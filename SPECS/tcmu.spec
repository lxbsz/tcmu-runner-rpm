# This is for tumu-runner
%global __spec_install_pre %{___build_pre}
%define debug_package %{nil}

%define dist .el7

%define rpmversion 1.3.0
%define pkgrelease rc3

%define pkg_release %{specrelease}%{?buildid}

Summary: The tcmu runner
Name: tcmu-runner
Group: System Environment/Kernel
License: Apache 2.0
URL: https://github.com/open-iscsi/tcmu-runner
Version: %{rpmversion}
Release: %{pkgrelease}%{dist}
Vendor: Chinamobile Co,Ltd

# Only in linux for now
ExclusiveOS: Linux

#
# List the packages used during the kernel build
#
BuildRequires: cmake, make, gcc, libnl3-devel, glib2-devel, tar, zlib-devel
BuildRequires: glusterfs-api-devel, zlib-devel, librados2-devel, librbd1-devel, kmod-devel

Requires(pre): librados2, librbd1, kmod, zlib, libnl3, glib2, glusterfs-api

Source0: tcmu-runner-%{rpmversion}.tar.gz

BuildRoot: %{_topdir}/BUILDROOT

%description
LIO passthough in userspace

%prep
%setup -q

%build
cmake . -DSUPPORT_SYSTEMD=ON -DCMAKE_INSTALL_PREFIX=/usr
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root, 0755)
/usr/bin/tcmu-runner
%defattr(-,root,root, 0644)
/etc/dbus-1/system.d/*
/etc/tcmu/*
/usr/lib/systemd/system/*
/usr/lib64/*
/usr/share/dbus-1/system-services/*
/usr/share/man/man8/*

%clean
rm -rf $RPM_BUILD_ROOT

