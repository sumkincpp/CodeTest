#ESXi compatible vmdk
qemu-img convert -f qcow2 -O vmdk -o adapter_type=lsilogic,subformat=streamOptimized,compat6 from.qcow2 to.vmdk

# OR
qemu-img convert -f qcow2 myImage.qcow2 -O vmdk myNewImage.vmdk 
vmkfstools -i myImage.vmdk outputName.vmdk -d thin
