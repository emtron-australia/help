# Get all Newtopic*.md files
$files = Get-ChildItem 'c:\Users\phil_\dev\online-help\content\engine-management\uncategorised\Newtopic*.md' | Sort-Object Name

$mapping = @()
$count = 0

foreach ($file in $files) {
    $count++
    if ($count % 50 -eq 0) { Write-Host "Processing file $count of $($files.Count)..." }

    $originalName = $file.Name
    $content = Get-Content $file.FullName -Raw -ErrorAction SilentlyContinue

    # Extract title from content
    $title = ""
    $description = ""

    if ($content) {
        # Try to find a # heading
        $lines = $content -split "`n"
        foreach ($line in $lines) {
            if ($line -match '^\s*#+\s+(.+)$') {
                $title = $matches[1].Trim('# ').Trim()
                break
            }
            # If no heading, use first non-empty line
            elseif ($line.Trim() -and -not $title) {
                $title = $line.Trim()
                break
            }
        }

        # Get description (first 100 chars after title)
        $firstContent = $lines | Where-Object { $_.Trim() -and -not ($_ -match '^\s*#+') } | Select-Object -First 1
        if ($firstContent) {
            $description = $firstContent.Substring(0, [Math]::Min(100, $firstContent.Length)).Trim()
        }
    }

    # Generate safe filename
    if ($title) {
        $safeName = $title.ToLower() `
            -replace '[^a-z0-9\s-]', '' `
            -replace '\s+', '-' `
            -replace '-+', '-' `
            -replace '^-|-$', ''
        if ($safeName.Length -eq 0) {
            $safeName = 'placeholder-empty'
        }
    } else {
        $safeName = 'placeholder-empty'
        $title = '[EMPTY FILE]'
    }

    $safeName = "$($safeName).md"

    $mapping += @{
        originalFilename = $originalName
        suggestedFilename = $safeName
        title = $title
        description = if ($description) { $description } else { '[No content]' }
    }
}

Write-Host "Total files processed: $count"
$mapping | ConvertTo-Json -Depth 10 | Out-File 'c:\Users\phil_\dev\online-help\newtopic-mapping.json'
Write-Host "Mapping saved to newtopic-mapping.json"
