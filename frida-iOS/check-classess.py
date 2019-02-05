#!/usr/bin/env python3
#!cording=utf-8

"""
Get classes and method
Tested on iOS 11.4.1(With Jailbreak)
Author:yotti(kusama yoshiki)
"""


import sys
import frida

get_information = """
if(ObjC.available)
{
    for(var className in ObjC.classes)
    {
        for(ObjC.classes.hasOwnProperty(className))
        {
            console.log(className);
            }
        }
}
else
{
    console.log("it is not available");
}
"""

device = frida.get_usb_device()
pid = device.spawn("Twitter")
session = device.attach(pid)
script = session.create_script(get_information)
script.load()
device.resume(pid)
sys.stdin.read()
