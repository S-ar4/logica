mortis=267
ruffs=565
emz=897
shelly=153
squeak=910

if(mortis > ruffs and mortis > emz and mortis > shelly and mortis > squeak ):
    print(mortis)
elif(ruffs > mortis and ruffs > emz and ruffs > shelly and ruffs > squeak):
    print(ruffs)
elif(emz > mortis and emz > ruffs and emz > shelly and emz > squeak):
    print(emz)
elif(shelly > mortis and shelly > ruffs and shelly > emz and emz > squeak):
    print(shelly)
else: 
    print(squeak)
