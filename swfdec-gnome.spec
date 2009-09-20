%define name swfdec-gnome
%define version 2.26.0
%define swfdec_version 0.8.0

%define release %mkrel 2

Summary: Flash integration for the Gnome Desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://swfdec.freedesktop.org/
BuildRequires: swfdec-devel >= %{swfdec_version}
BuildRequires: libGConf2-devel
BuildRequires: gtk2-devel >= 2.12.0
BuildRequires: intltool

%description
Swfdec-Gnome provides tools to integrate Flash into the GNOME desktop.
It contains a standalone Flash player and a thumbnailer.

%prep
%setup -q

%build
%configure2_5x --disable-schemas-install
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post
%post_install_gconf_schemas swfdec-thumbnailer
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%preun
%preun_uninstall_gconf_schemas swfdec-thumbnailer

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%{_sysconfdir}/gconf/schemas/swfdec-thumbnailer.schemas
%{_bindir}/swfdec-player
%{_bindir}/swfdec-thumbnailer
%{_datadir}/applications/swfdec-player.desktop
%{_datadir}/swfdec-gnome/swfdec-player.ui
%{_mandir}/man1/*
%_datadir/icons/hicolor/*/apps/*
