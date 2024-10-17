Summary: Client for Last.fm and compatible music streaming services
Name: vagalume
Version: 0.8.6
Release: 1
Source0: http://vagalume.igalia.com/files/source/%{name}-%{version}.tar.gz
License: GPLv3
Group: Sound
Url: https://vagalume.igalia.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxml2-devel
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gstreamer-plugins-base-1.0)
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
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README AUTHORS THANKS TODO TRANSLATORS
%_bindir/%name
%_bindir/vagalumectl
%_datadir/pixmaps/%name.xpm
%_datadir/man/man1/*
%_datadir/applications/%name.desktop
%_datadir/%name
%_datadir/icons/hicolor/*/apps/%name.*
%_datadir/dbus-1/services/%name.service
