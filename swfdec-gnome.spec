%define name swfdec-gnome
%define version 2.30.1
%define swfdec_version 0.8.0

%define release 3

Summary: Flash integration for the Gnome Desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
License: GPLv2+
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: https://swfdec.freedesktop.org/
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


%changelog
* Sun May 22 2011 Funda Wang <fwang@mandriva.org> 2.30.1-2mdv2011.0
+ Revision: 677123
- rebuild to add gconf2 as req

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.30.1-1mdv2011.0
+ Revision: 581763
- update to new version 2.30.1

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 528965
- update to new version 2.30.0

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.28.0-1mdv2010.0
+ Revision: 446958
- update to new version 2.28.0

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 2.26.0-2mdv2010.0
+ Revision: 445300
- rebuild

* Mon Mar 16 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 355979
- update to new version 2.26.0
- fix source URL

* Tue Sep 23 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 287361
- new version

* Mon Sep 08 2008 Götz Waschk <waschk@mandriva.org> 2.23.4-1mdv2009.0
+ Revision: 282628
- new version
- bump swfdec dep

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.23.2-2mdv2009.0
+ Revision: 269399
- rebuild early 2009.0 package (before pixel changes)

* Fri Aug 08 2008 Götz Waschk <waschk@mandriva.org> 2.23.2-1mdv2009.0
+ Revision: 267921
- new version
- update deps
- update file list

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat May 17 2008 Funda Wang <fwang@mandriva.org> 2.22.2-1mdv2009.0
+ Revision: 208509
- New version 2.22.2

* Sat Mar 01 2008 Michael Scherer <misc@mandriva.org> 2.21.91-1mdv2008.1
+ Revision: 177093
- new version
- use macro instead of duplicating version
- use gz, as this is used uptream

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Fri Feb 01 2008 Frederic Crozat <fcrozat@mandriva.com> 2.21.90-1mdv2008.1
+ Revision: 161141
- Release 2.21.90

* Wed Dec 19 2007 Nicholas Brown <nickbrown@mandriva.org> 0.5.5-1mdv2008.1
+ Revision: 133951
- import swfdec-gnome


