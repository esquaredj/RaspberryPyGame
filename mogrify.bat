@echo off
for /r /d %%d in (*) do (
    pushd "%%d"
    mogrify *.png
    popd
)

