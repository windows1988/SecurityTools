#!/usr/bin/env python3
#!cording=utf-8

"""
Get classes and method
Tested on iOS 11.4.1(With Jailbreak)
Author:yotti(kusama yoshiki)
"""


import sys
import frida
"""
get_method_information = 
var className = "JailbreakDetection";
if (ObjC.available)
{
    for (var className in ObjC.classes)
    {
        if (ObjC.classes.hasOwnProperty(className))
        {
            console.log("[+] Class: " + className);
            var methods = eval('ObjC.classes.' + className + '.$methods');
            for (var i = 0; i < methods.length; i++)
            {
                console.log("\t[-] Method: "+methods[i]);
            }
        }
    }
}
else
{
    console.log("not running");
}
"""


get_method_information = """
if(ObjC.available){
try
{
    var className = "JailbreakDetection";
    var methods = eval('ObjC.classes.' + className + '.$methods');
    for (var i = 0; i < methods.length; i++){
        try{
            console.log("[-] "+methods[i]);
        }
        catch(err){
            console.log("[!] Exception1: " + err.message);
        }
    }
}
catch(err){
    console.log("[!] Exception2: " + err.message);
}}
else{
    console.log("not running maybe...");
}
"""



session = frida.get_usb_device().attach('DVIA-v2')
script = session.create_script(get_method_information)
print("[*]start scan")
script.load()
print("[*]end scan")
sys.stdin.read()
script.exit()
