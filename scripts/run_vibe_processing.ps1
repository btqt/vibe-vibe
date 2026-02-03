<#
.SYNOPSIS
    Script to sequentially run Python scripts for processing Markdown files.
    
.DESCRIPTION
    This script executes 2 python scripts in order:
    1. rewrite_vi_links.py: Rewrites links in Vietnamese Markdown files.
    2. md_to_html.py: Converts markdown to HTML.

.PARAMETER TargetDir
    The root directory to scan for files. Mandatory.
    
.EXAMPLE
    .\run_vibe_processing.ps1 -TargetDir "C:\path\to\docs"
#>

[CmdletBinding()]
param (
    [Parameter(Mandatory=$true, Position=0, HelpMessage="Please specify the root directory to scan.")]
    [string]$TargetDir
)

# Get the directory of the current script
$ScriptDir = $PSScriptRoot

Write-Host "--------------------------------------------------" -ForegroundColor Cyan
Write-Host "Starting Vibe Vibe processing workflow..." -ForegroundColor Cyan
Write-Host "Target Directory: $TargetDir" -ForegroundColor Cyan
Write-Host "--------------------------------------------------" -ForegroundColor Cyan

# Check if TargetDir exists
if (-not (Test-Path -Path $TargetDir -PathType Container)) {
    Write-Error "Error: The directory '$TargetDir' does not exist."
    exit 1
}

# ----------------------------------------------------------------
# Bước 1: Chạy script rewrite_vi_links.py
# ----------------------------------------------------------------
$Script1 = "rewrite_vi_links.py"
$Script1Path = Join-Path -Path $ScriptDir -ChildPath $Script1

Write-Host "Running $Script1 ..." -ForegroundColor Yellow

if (Test-Path $Script1Path) {
    # Call python to run script with the target directory
    # rewrite_vi_links.py takes root_dir as argument
    python $Script1Path $TargetDir
    
    # Check exit code (0 is success)
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[OK] $Script1 completed successfully." -ForegroundColor Green
    } else {
        Write-Host "[ERROR] $Script1 encountered an error (Exit code: $LASTEXITCODE)." -ForegroundColor Red
        # Uncomment to stop on error
        # exit $LASTEXITCODE 
    }
} else {
    Write-Host "[WARN] File $Script1 not found at $Script1Path" -ForegroundColor Red
}

Write-Host "--------------------------------------------------" -ForegroundColor Gray

# ----------------------------------------------------------------
# Step 2: Run md_to_html.py
# ----------------------------------------------------------------
$Script2 = "md_to_html.py"
$Script2Path = Join-Path -Path $ScriptDir -ChildPath $Script2

Write-Host "Running $Script2 ..." -ForegroundColor Yellow

if (Test-Path $Script2Path) {
    # Call python to run script with target directory and --recursive flag
    python $Script2Path $TargetDir --recursive
    
    # Check exit code
    if ($LASTEXITCODE -eq 0) {
        Write-Host "[OK] $Script2 completed successfully." -ForegroundColor Green
    } else {
        Write-Host "[ERROR] $Script2 encountered an error (Exit code: $LASTEXITCODE)." -ForegroundColor Red
        exit $LASTEXITCODE
    }
} else {
    Write-Host "[WARN] File $Script2 not found at $Script2Path" -ForegroundColor Red
}

Write-Host "--------------------------------------------------" -ForegroundColor Cyan
Write-Host "All processing steps finished." -ForegroundColor Cyan
Write-Host "--------------------------------------------------" -ForegroundColor Cyan
