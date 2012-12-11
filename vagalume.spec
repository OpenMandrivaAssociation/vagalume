%define name vagalume
%define version 0.8.5
%define release %mkrel 1

Summary: Client for Last.fm and compatible music streaming services
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://vagalume.igalia.com/files/source/%{name}-%{version}.tar.gz
License: GPLv3
Group: Sound
Url: http://vagalume.igalia.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgstreamer-plugins-base-devel
BuildRequires: libxml2-devel
BuildRequires: gtk+2-devel
#gw or:
#BuildRequires: gtk+2-devel
BuildRequires: curl-devel
BuildRequires: dbus-glib-devel
BuildRequires: libnotify-devel >= 0.4.1
BuildRequires: libproxy-devel
BuildRequires: intltool


%description
Vagalume is a Last.fm client written using GTK+. 
Its main features are:
 * It plays Last.fm radio streams (using the v2.0 API)
 * It supports Libre.fm and other compatible servers
 * Support for different radio stations (personal, neighbours, loved tracks 
  or any lastfm:// URL)
 * It supports marking tracks as loved or banned
 * It can tag artists, tracks and albums
 * It can send recommendations to other users
 * It can add tracks to your playlist
 * It can download free tracks to your hard disk
 * It scrobbles tracks so they appear in your Last.fm webpage

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %name

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc README AUTHORS THANKS TODO TRANSLATORS
%_bindir/%name
%_bindir/vagalumectl
%_datadir/pixmaps/%name.xpm
%_datadir/man/man1/*
%_datadir/applications/%name.desktop
%_datadir/%name
%_datadir/icons/hicolor/*/apps/%name.*
%_datadir/dbus-1/services/%name.service





%changelog
* Tue Jul 12 2011 Götz Waschk <waschk@mandriva.org> 0.8.5-1mdv2011
+ Revision: 689678
- import vagalume

