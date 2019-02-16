# Offloading and turning of Kernel same-page merging
echo 2 >/sys/kernel/mm/ksm/run
echo 0 >/sys/kernel/mm/ksm/merge_across_nodes
