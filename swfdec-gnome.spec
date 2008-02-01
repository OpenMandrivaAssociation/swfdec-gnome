%define name swfdec-gnome
%define version 2.21.90
%define swfdec_version 0.5.90

%define major 0.5
%define release %mkrel 1

Summary: Flash integration for the Gnome Desktop
Name: %{name}
Version: 2.21.90
Release: %{release}
Source0: http://download.gnome.org/sources/swfdec-gnome/%{name}-%{version}.tar.bz2
License: GPL
Group: Graphical desktop/GNOME
Url: http://swfdec.freedesktop.org/
BuildRequires: swfdec-devel >= %{swfdec_version}
BuildRequires: libGConf2-devel
BuildRequires: gtk2-devel >= 2.12.0
BuildRequires: perl-XML-Parser

%description
Swfdec-Gnome provides tools to integrate Flash into the GNOME desktop.
It contains a standalone Flash player and a thumbnailer.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%post_install_gconf_schemas swfdec-thumbnailer
%{update_menus}
%{update_desktop_database}

%preun
%preun_uninstall_gconf_schemas swfdec-thumbnailer
%postun
%{clean_menus}
%{clean_desktop_database}

%files -f %{name}.lang
%defattr(-,root,root)
%{_sysconfdir}/gconf/schemas/swfdec-thumbnailer.schemas
%{_bindir}/swfdec-player
%{_bindir}/swfdec-thumbnailer
%{_datadir}/applications/swfdec-player.desktop
%{_datadir}/swfdec-gnome/swfdec-player.ui
%{_mandir}/man1/*
