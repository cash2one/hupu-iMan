#region ;**** 参数创建于 ACNWrapper_GUI ****
#PRE_icon=C:\windows\SYSTEM32\SHELL32.dll|-46
#PRE_Outfile=E:\cody\hupu-iMan\tools\upload.exe
#PRE_UseX64=n
#PRE_Res_Comment=cody.guo 用于上传文件
#PRE_Res_Description=cody.guo 用于上传文件
#PRE_Res_Fileversion=3.1.1.0
#PRE_Res_LegalCopyright=上海互普信息技术有限公司
#PRE_Run_Tidy=y
#endregion ;**** 参数创建于 ACNWrapper_GUI ****
; ControlFocus("title", "text", controlID) Edit1=Edit instance 1

$status = $cmdline[1]
;$cmdline[1]

If $cmdline[0] <> 2 Then Exit MsgBox(48, "警告", "有且只能有1个参数！")

Select
	Case $status = 1
		ControlClick("文件上传", "", "Button1")
		;ControlClick("选择要加载的文件", "", "Button1")
		;ControlClick("打开", "", "Button1")

		MsgBox(0, "提示", "正在运行关闭.")
	Case $status = 2
		; Wait 10 seconds for the Upload windows to appear
		Sleep(6000)
		While True
			If WinExists("文件上传", "") Then
				WinActivate("文件上传")
				
				; MsgBox(0, "hello", "已存在.")
				Local $fileclass = WinWait("文件上传", "", 30)
				ControlFocus($fileclass, "", "Edit1")
				
				; Set the File name text on the Edit field
				ControlSetText("文件上传", "", "Edit1", $cmdline[2])
				
				; "d:\Users\cody.guo\Desktop\c0ed1049-bdd5-44da-a696-04e5625d577c"
				; Click on then Open button
				ControlClick("文件上传", "", "Button1")
				;MsgBox(0, "提示", "正在运行.")
				ExitLoop
			ElseIf WinExists("选择要加载的文件", "") Then
				WinActivate("选择要加载的文件")
				;WinWaitActive("选择要加载的文件", "", 30)
				Local $fileclass = WinWait("选择要加载的文件", "", 30)
				ControlFocus($fileclass, "", "Edit1")
				ControlSetText("选择要加载的文件", "", "Edit1", $cmdline[2])
				Sleep(3)
				ControlClick("选择要加载的文件", "", "Button1")
				ExitLoop
			ElseIf WinExists("打开", "") Then
				WinActivate("打开")
				;WinWaitActive("打开", "", 30)
				Local $fileclass = WinWait("打开", "", 30)
				ControlFocus($fileclass, "", "Edit1")
				ControlSetText("打开", "", "Edit1", $cmdline[2])
				Sleep(3)
				ControlClick("打开", "", "Button1")
				ExitLoop
			EndIf
		WEnd
EndSelect
