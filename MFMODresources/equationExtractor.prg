'##############################################################################
' Subroutines  to the export model information to text files
'##############################################################################

subroutine extract_equations(string %folder)
    'test
    %stoch={%cty}.@stochastic
    %stoch = @wdrop(%stoch, "*_M")

    %extra=%cty+"SBBEXP" + " " + %cty + "SBBREV"

    %linked = {%cty}.@linklist
    string x = %stoch
    %idents={%cty}.@identity
    %idents = @wdrop(%idents, %cty+"NYGDPMKTPKP")           '''Real GDP PPP

    delete(noerr) mod_spec

    table(1000,1) mod_spec

    scalar r=1

    mod_spec(r,1) = "' From here build model"
    'mod_spec(r+2,1) = "model " + %cty

    r=r+4

    for %var {%stoch}
        %varunderscore = "_" + %var
        if @wfind(%linked, %varunderscore) then
            mod_spec(r,1) = "smpl "+ {%varunderscore}.@smpl
            mod_spec(r+1,1)="equation _"+%var+".ls(optmethod=legacy) "+ {%varunderscore}.@spec
        else
            mod_spec(r+1,1)=%cty+".append "+{%cty}.@spec(%var)
        endif
        r=r+3
    next
    for %var {%extra}
        %varunderscore = "_" + %var
        %objInWF = @wlookup(%varunderscore, "equation")
        if @len(%objInWF) then
            mod_spec(r,1) = "smpl "+ {%varunderscore}.@smpl
            mod_spec(r+1,1)="equation _"+%var+".ls(optmethod=legacy) "+ {%varunderscore}.@spec
            r=r+3
        endif
    next

    r=r+2

    'mod_spec(r,1)=" '    Identity equations --------------------------------------"
    r=r+2

    for %var {%idents}
        %temp={%cty}.@spec(%var)
        mod_spec(r,1)=%cty+".append @identity "+%temp
        r=r+2
    next

    'save to modelDetails folder
    shell IF exist %folder (echo directory exists) ELSE ( mkdir %folder )
    if @isobject("pulled") then
        %equationsPath = %folder + %cty + "pulledequations.prg"
        delete pulled
    else
        %equationsPath = %folder + %cty + "equations.prg"
    endif
    mod_spec.save(t=txt) %equationsPath
endsub

subroutine extract_estimated_equations(string %folder)
    string solvedeqs = {%cty}.@stochastic
    delete(noerr) eqlist
    table(200, 50) eqlist
    !r = 1
    for %eqn in {solvedeqs}
         if @isobject("_"+%eqn) then
            eqlist(!r,1) = "equation" + " _" + %eqn + " " +  _{%eqn}.@subst
            for !i=1 to @rows(_{%eqn}.@pvals)
                eqlist(!r+1,1) = "p-values"
                eqlist(!r+1,!i+1) = _{%eqn}.@pvals(!i)
            next
            !r = !r+3
         endif
    next
    'save to modelDetails folder
    shell IF exist %folder (echo directory exists) ELSE ( mkdir %folder )
    %estimatedEquationsPath = %folder + %cty + "estimatedEquations.prg"
    eqlist.save(t=txt) %estimatedEquationsPath
endsub

subroutine extract_series(string %folder)
    %srlist = @wkeep(@wlookup("*", "series"),%cty+"*")
    delete(noerr) srspec
    table(200,10) srspec
    !r = 1
    for !i = 1 to @wcount(%srlist)
        %sr = @word(%srlist, !i)
        %histor = {%sr}.@attr("History")
        if @rinstr(%histor, "=>") then
            %srdef = @trim(@right(%histor, @length(%histor) - @rinstr(%histor, "=>") - 1))
            srspec(r, 1) = "series " + %srdef
            r = r+2
        endif
    next
    shell IF exist %folder (echo directory exists) ELSE ( mkdir %folder )
    %seriesPath = %folder + %cty + "series_spec.prg"
    srspec.save(t=txt) %seriesPath
endsub

subroutine create_variable_dictionary(string %folder)
    string stochlist = {%cty}.@stochastic
    string identlist = {%cty}.@identity
    if @isobject("c_spec_qi") then
        string cty_c_spec_qi = @wreplace(c_spec_qi, "*", %cty+"*")
    else
        string cty_c_spec_qi = " "
    endif
    string variablesRaw = {%cty}.@varlist
    string variablesClean = @wdrop(variablesRaw, "*_A")

    !tableLength = @wcount(variablesClean)*4
    table(!tableLength,1) vartab

    !i = 1
    for %var {variablesClean}
        %deps = {%cty}.@depends(%var)
        %ups = {%cty}.@upends(%var)
        if @wfind(stochlist, %var) then
            %cleanDeps = @wdrop(%deps, "*_A")
            if @wfind(cty_c_spec_qi, %var) then
                vartab(!i,1) = %var + ":"
                !i = !i+1
                vartab(!i,1) = "  type: quasi-identity"
                !i = !i+1
                vartab(!i,1) = "  dependencies: "  + %cleanDeps
                !i = !i+1
                vartab(!i,1) = "  varsDependingOn: "  + %ups
            else
                vartab(!i,1) = %var + ":"
                !i = !i+1
                vartab(!i,1) = "  type: stochastic" 
                !i = !i+1
                vartab(!i,1) = "  dependencies: " + %cleanDeps
                !i = !i+1
                vartab(!i,1) = "  varsDependingOn: "  + %ups
            endif
        else
            if @wfind(identlist, %var) then
                vartab(!i,1) = %var +":"
                !i=!i+1
                vartab(!i,1) = "  type: identity"
                !i=!i+1
                vartab(!i,1) = "  dependencies: " +  %deps
                !i = !i+1
                vartab(!i,1) = "  varsDependingOn: "  + %ups
            else
                vartab(!i,1) = %var + ":"
                !i=!i+1
                vartab(!i,1) = "  type: exogenous"
                !i=!i+1
                vartab(!i,1) = "  dependencies: null"
                !i = !i+1
                vartab(!i,1) = "  varsDependingOn: "  + %ups
            endif
        endif
        !i = !i + 1
    next


    shell IF exist %folder (echo directory exists) ELSE ( mkdir %folder )

    %varDictPath = %folder + %cty + "MODvars.yml"
    vartab.save(t=txt) %varDictPath
endsub
