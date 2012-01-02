# Copyright (c) 2008 SuSE Linux Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

# norootforbuild

Name:         pearpc
License:      GPL
Group:        unsorted
Autoreqprov:  on
Version:      0.4
Release:      4.18
Summary:      PowerPC platform emulator
Source:       %name-%version.tar.bz2
Patch:        stupidcast.patch
Patch1:       jittypo.patch
Patch2:       pearpc-rpmlint.patch
BuildRequires: SDL-devel nasm gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PearPC is an architecture-independent PowerPC platform emulator capable of running most PowerPC operating systems.

%prep
%setup
%patch
%patch1
%patch2

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr --enable-ui=sdl --mandir=%_mandir
make %{?jobs:-j%jobs}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc video.x ppccfg.example AUTHORS ChangeLog README TODO
/usr/bin/ppc
%doc %_mandir/man1/*

