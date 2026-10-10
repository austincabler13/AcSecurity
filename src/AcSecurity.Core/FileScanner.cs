using System.IO;

namespace AcSecurity.Core;

public class FileScanner
{
    public bool FileExists(string path)
    {
        return File.Exists(path);
    }
}