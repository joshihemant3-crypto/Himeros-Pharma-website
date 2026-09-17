$refAssemblies = @(
    "C:\Windows\System32\WinMetadata\Windows.Foundation.winmd",
    "C:\Windows\System32\WinMetadata\Windows.Media.winmd",
    "C:\Windows\System32\WinMetadata\Windows.Graphics.winmd",
    "C:\Windows\System32\WinMetadata\Windows.Storage.winmd"
)

$csharp = @"
using System;
using System.Threading.Tasks;
using Windows.Graphics.Imaging;
using Windows.Media.Ocr;
using Windows.Storage;

public class WinOcr {
    public static string DoOcr(string path) {
        return Task.Run(async () => {
            StorageFile file = await StorageFile.GetFileFromPathAsync(path);
            using (var stream = await file.OpenAsync(FileAccessMode.Read)) {
                BitmapDecoder decoder = await BitmapDecoder.CreateAsync(stream);
                SoftwareBitmap bitmap = await decoder.GetSoftwareBitmapAsync();
                OcrEngine engine = OcrEngine.TryCreateFromUserProfileLanguages();
                OcrResult result = await engine.RecognizeAsync(bitmap);
                return result.Text;
            }
        }).GetAwaiter().GetResult();
    }
}
"@

Add-Type -TypeDefinition $csharp -ReferencedAssemblies $refAssemblies -Language CSharp

$files = Get-ChildItem -Path "items\*gallery*.png", "items\*goa*.png", "Gallery\ANDROCON-Hyderabad\androcon_cover.png"
foreach ($f in $files) {
    Write-Host "=== FILE: $($f.Name)"
    try {
        $text = [WinOcr]::DoOcr($f.FullName)
        Write-Host $text
    } catch {
        Write-Host "Error: $_"
    }
}
