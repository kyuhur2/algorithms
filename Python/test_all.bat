@echo off

FOR /D %%i IN (*) DO (
    @echo %%i
    pushd %%i
    FOR %%j IN (*.py) DO (
        @echo %%j
        python %%j
        echo[
    )
    popd
    echo[
)
