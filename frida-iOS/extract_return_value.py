#!/usr/bin/env python3
#!cording=utf-8

"""
Get classes and method
Tested on iOS 11.4.1(With Jailbreak)
Author:yotti(kusama yoshiki)
"""


import sys
import frida


get_return_value_from_method = """
if (ObjC.available){
    try
    {
        //Your class name here
        var className = "ViewController";
        //Your function name here
        var funcName = "Jailbreak()";
        var hook = eval('ObjC.classes.' + className + '["' + funcName + '"]');
        Interceptor.attach(hook.implementation, {
          onLeave: function(retval) {
            console.log("[*] Class Name: " + className);
            console.log("[*] Method Name: " + funcName);
            console.log("\t[-] Type of return value: " + typeof retval);
            //console.log(retval.toString());
            console.log("\t[-] Return Value: " + retval);
            //For modifying the return value
            //newretval = ptr("0x0") //your new return value here
            //retval.replace(newretval)
            //console.log("\t[-] New Return Value: " + newretval)
          }
        });
    }
    catch(err)
    {
        console.log("[!] Exception2: " + err.message);
    }
}
else{
    console.log("Objective-C Runtime is not available!");
}
"""
session = frida.get_usb_device().attach('JailbreakDetection')
script = session.create_script(get_return_value_from_method)
print("[*]start scan")
script.load()
print("[*]end scan")
sys.stdin.read()
script.exit()
