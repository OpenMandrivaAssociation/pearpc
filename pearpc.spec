%define Werror_cflags %nil
Name:         pearpc
License:      GPL
Group:        Emulators
Version:      0.5
Release:      %mkrel 1
Summary:      PowerPC platform emulator
Source:       %name-%version.tar.bz2
BuildRequires: SDL-devel nasm gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
PearPC is an architecture-independent PowerPC platform emulator capable of running most PowerPC operating systems.

%prep
%setup

%build
%configure --enable-ui=sdl
make 

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc video.x ppccfg.example AUTHORS ChangeLog README TODO
%{_bindir}/ppc
%doc %_mandir/man1/*

