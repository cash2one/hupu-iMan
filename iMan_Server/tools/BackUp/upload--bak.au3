#region ;**** ���������� ACNWrapper_GUI ****
#PRE_icon=C:\windows\SYSTEM32\SHELL32.dll|-46
#PRE_Outfile=E:\cody\hupu-iMan\tools\upload.exe
#PRE_UseX64=n
#PRE_Res_Comment=cody.guo �����ϴ��ļ�
#PRE_Res_Description=cody.guo �����ϴ��ļ�
#PRE_Res_Fileversion=3.1.1.0
#PRE_Res_LegalCopyright=�Ϻ�������Ϣ�������޹�˾
#PRE_Run_Tidy=y
#endregion ;**** ���������� ACNWrapper_GUI ****
; ControlFocus("title", "text", controlID) Edit1=Edit instance 1

$status = $cmdline[1]
;$cmdline[1]

If $cmdline[0] <> 2 Then Exit MsgBox(48, "����", "����ֻ����1��������")

Select
	Case $status = 1
		ControlClick("�ļ��ϴ�", "", "Button1")
		;ControlClick("ѡ��Ҫ���ص��ļ�", "", "Button1")
		;ControlClick("��", "", "Button1")

		MsgBox(0, "��ʾ", "�������йر�.")
	Case $status = 2
		; Wait 10 seconds for the Upload windows to appear
		Sleep(6000)
		While True
			If WinExists("�ļ��ϴ�", "") Then
				WinActivate("�ļ��ϴ�")
				
				; MsgBox(0, "hello", "�Ѵ���.")
				Local $fileclass = WinWait("�ļ��ϴ�", "", 30)
				ControlFocus($fileclass, "", "Edit1")
				
				; Set the File name text on the Edit field
				ControlSetText("�ļ��ϴ�", "", "Edit1", $cmdline[2])
				
				; "d:\Users\cody.guo\Desktop\c0ed1049-bdd5-44da-a696-04e5625d577c"
				; Click on then Open button
				ControlClick("�ļ��ϴ�", "", "Button1")
				;MsgBox(0, "��ʾ", "��������.")
				ExitLoop
			ElseIf WinExists("ѡ��Ҫ���ص��ļ�", "") Then
				WinActivate("ѡ��Ҫ���ص��ļ�")
				;WinWaitActive("ѡ��Ҫ���ص��ļ�", "", 30)
				Local $fileclass = WinWait("ѡ��Ҫ���ص��ļ�", "", 30)
				ControlFocus($fileclass, "", "Edit1")
				ControlSetText("ѡ��Ҫ���ص��ļ�", "", "Edit1", $cmdline[2])
				Sleep(3)
				ControlClick("ѡ��Ҫ���ص��ļ�", "", "Button1")
				ExitLoop
			ElseIf WinExists("��", "") Then
				WinActivate("��")
				;WinWaitActive("��", "", 30)
				Local $fileclass = WinWait("��", "", 30)
				ControlFocus($fileclass, "", "Edit1")
				ControlSetText("��", "", "Edit1", $cmdline[2])
				Sleep(3)
				ControlClick("��", "", "Button1")
				ExitLoop
			EndIf
		WEnd
EndSelect
