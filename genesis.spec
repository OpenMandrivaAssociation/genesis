%define         svn       866326

Name: genesis
Summary: Application Lifecycle Manager
Version: 0.0.1
Release: %mkrel 0.1
Url: http://www.moblin.org/projects/genesis-application-lifecycle-manager
License: LGPLv2+
Group: Graphical desktop/KDE
BuildRoot: %{_tmppath}/%{name}-%{version}-build
# From GIT http://git.moblin.org/repos/users/horace.li/genesis.git
Source0: %name-%version.tar.bz2
Patch0: genesis-0.0.1-disable-fortify-warning.patch
Patch1: genesis-0.0.1-version-info.patch
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: libwnck-1-devel
BuildRequires: libxml2-devel
BuildRequires: gtk+2-devel
BuildRequires: pkgconfig

%description
This project is part of the Moblin application framework, exposing interface for application developers to conveniently access application information, starting an application by calling a single API, and processing various run-time statuses for each running application.

%files
%defattr(-,root,root)
%_bindir/*

#--------------------------------------------------------------------

%define gen_soname 0
%define libgenesis %mklibname genesis %{gen_soname}

%package -n %{libgenesis}
Summary: Moblin genesis library
Group: System/Libraries

%description -n %{libgenesis}
Moblin genesis library.

%files -n %{libgenesis}
%defattr(-,root,root)
%_libdir/libgenesis.so.%{gen_soname}*

#--------------------------------------------------------------------

%define libdev %mklibname genesis -d

%package -n %{libdev}
Summary: Moblin genesis library devel files
Group: System/Libraries
Requires: %{libgenesis} = %{version}

%description -n %{libdev}
Moblin genesis library devel files.

%files -n %{libdev}
%defattr(-,root,root)
%_libdir/*.so
%_libdir/*.la
%_libdir/pkgconfig/*.pc
%_includedir/*

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .fortify
%patch1 -p0 -b .version_info

%build
NOCONFIGURE=true sh autogen.sh

%configure \
    --disable-static

%make

%install
rm -fr %buildroot
%makeinstall_std 


%clean
rm -rf "%{buildroot}"
