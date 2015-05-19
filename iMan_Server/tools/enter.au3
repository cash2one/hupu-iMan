#Region ;**** 参数创建于 ACNWrapper_GUI ****
#PRE_Icon=C:\windows\SYSTEM32\SHELL32.dll
#PRE_Outfile=enter.exe
#PRE_UseX64=n
#PRE_Res_Fileversion=0.0.0.0
#EndRegion ;**** 参数创建于 ACNWrapper_GUI ****


; MsgBox(0, "hello", "已存在.")
;Local $fileclass = WinWait("Windows安全", "", 30)
;ControlFocus($fileclass, "", "Button2")

; "d:\Users\cody.guo\Desktop\c0ed1049-bdd5-44da-a696-04e5625d577c"
; Click on then Open button
ControlClick("Windows安全", "", "Button2")
;MsgBox(0, "提示", "正在运行.")