# hopper_Kernelcache_symbol

This is a Hopper Disassembler Python script used to restore kernelcache symbols. Modified from the [Ghidra kernelcache](https://github.com/0x36/ghidra_kernelcache). Requires at the first stage [iometa](https://github.com/Siguza/iometa/) (made by @s1guza) 

## Usage

After decompressing the kernel, run the following commands :

```shell
iometa -n -A /tmp/kernel A10-legacy.txt > /tmp/kernel.txt
```

Load the kernelcache in Hopper Disassembler, open script editor, add `restore_symbol.py`. Run the script, select the kernel.txt and wait.