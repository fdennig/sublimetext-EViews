' ==============================
' DOWNLOAD COMMODITY DATA
' CJ
' ==============================
close @all
logmode l

%link = https://thedocs.worldbank.org/en/doc/5d903e848db1d1b83e0ec8f744e55570-0350012021/related/CMO-Historical-Data-Monthly.xlsx

import %link range="Monthly Prices" colhead=2 namepos=first na="…" @freq M @id @date(series01) @smpl @all

' .@displayname
rename ALUMINUM WLDFALUMINUM
'rename BANANA__EUROPE Banana
rename BANANA__US WLDFBANANA_US 
''rename BARLEY 
rename BEEF WLDFBEEF
''rename CHICKEN 
'rename COAL__AUSTRALIAN___ 
rename COAL__SOUTH_AFRICAN___ WLDFCOAL_AUS
rename COCOA WLDFCOCOA
rename COCONUT_OIL 
rename COFFEE__ARABICA WLDFCOFFEE_COMPO
''rename COFFEE__ROBUSTA 
rename COPPER WLDFCOPPER
rename COTTON__A_INDEX WLDFCOTTON_A_INDX
''rename CRUDE_OIL__AVERAGE 
rename CRUDE_OIL__BRENT Oil
''rename CRUDE_OIL__DUBAI 
rename CRUDE_OIL__WTI WLDFCRUDE_PETRO
''rename DAP 
''rename FISH_MEAL 
rename GOLD WLDFGOLD
rename GROUNDNUT_OIL WLDFGRNUT_OIL
''rename GROUNDNUTS 
rename IRON_ORE__CFR_SPOT WLDFIRON_ORE
''rename LAMB___ 
''rename LEAD 
''rename LIQUEFIED_NATURAL_GAS__JAPAN 
''rename LOGS__CAMEROON 
rename LOGS__MALAYSIAN  WLDFLOGS_MYS
rename MAIZE WLDFMAIZE
rename NATURAL_GAS__EUROPE___ WLDFNGAS_EUR
'rename NATURAL_GAS__US 
'rename NATURAL_GAS_INDEX 
rename NICKEL  WLDFNICKEL
rename ORANGE WLDFORANGE
'rename PALM_KERNEL_OIL 
rename PALM_OIL WLDFPALM_OIL
'rename PHOSPHATE_ROCK 
'rename PLATINUM 
rename PLYWOOD WLDFPLYWOOD
'rename POTASSIUM_CHLORIDE 
'rename RAPESEED_OIL 
'rename RICE__THAI_25_ 
rename RICE__THAI_5_ WLDFRICE_05
'rename RICE__THAI_A_1 
'rename RICE__VIET_NAMESE_5_ 
rename RUBBER__SGP_MYS WLDFRUBBER1_MYSG
'rename RUBBER__TSR20 
'rename SAWNWOOD__CAMEROON 
rename SAWNWOOD__MALAYSIAN WLDFSAWNWD_MYS
'rename SHRIMPS__MEXICAN 
rename SILVER WLDFSILVER
rename SORGHUM WLDFSORGHUM
rename SOYBEAN_MEAL WLDFSOYBEAN_MEAL
rename SOYBEAN_OIL WLDFSOYBEAN_OIL
rename SOYBEANS WLDFSOYBEANS
'rename SUGAR__EU 
'rename SUGAR__US 
rename SUGAR__WORLD WLDFSUGAR_WLD
'rename SUNFLOWER_OIL 
rename TEA__AVG_3_AUCTIONS WLDFTEA_AVG
'rename TEA__COLOMBO 
'rename TEA__KOLKATA 
'rename TEA__MOMBASA 
'rename TIN 
rename TOBACCO__US_IMPORT_U_V_ WLDFTOBAC_US
'rename TSP 
'rename UREA 
rename WHEAT__US_HRW WLDFWHEAT_US_HRW
'rename WHEAT__US_SRW___ 
rename ZINC WLDFZINC

group wld wldf*
%wlds = wld.@members

pagecreate q 1960Q1 2022Q4

' Copy from months to quartely
pageselect Untitled1
for %a {%wlds}
     copy(c=average) Untitled\{%a} *
next
