using System.IO;
using AcSecurity.Cli;

namespace AcSecurity.Core;

public class FileScanner
{
    public bool FileExists(string path);
    public char fullPath = Console.ReadLine;
    {
        return File.Exists(path);
    }
}