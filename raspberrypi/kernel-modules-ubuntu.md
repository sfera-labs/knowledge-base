# Compile and Install Raspberry Pi kernel modules on Ubuntu

To compile and install [any of the kernel modules for our Pi-based boards and modules](https://github.com/orgs/sfera-labs/repositories?q=kernel-module) on Ubuntu, follow the same steps described in the specific kernel module's repo, but pay attention to the following differences:

The kernel headers are included in the package `linux-headers-raspi`, and some packages included by default in Rapberry Pi OS are not in Ubuntu, so run the following to install the requirements:

    sudo apt install git linux-headers-raspi make gcc

In Ubuntu the Device Tree files are located in `/boot/firmware/overlays/`, rather than `/boot/overlays/`. Install the module's Device Tree there after compilation:

    dtc -@ -Hepapr -I dts -O dtb -o <MODULE_NAME>.dtbo <MODULE_NAME>.dts
    sudo cp <MODULE_NAME>.dtbo /boot/firmware/overlays/

Finally, the `/boot/config.txt` file in RPi OS, corresponds to `/boot/firmware/usercfg.txt` in Ubuntu. Add the `dtoverlay=<MODULE_NAME>` line there to enable the module.

All the other installation steps and usage of the `/sys/class/` files are the same.
