%define	sname		flare_linux
%define	sversion	v015_1

Name:		flare
Version:	15.1
Release:	2
Summary:	Diablo-like role-playing game in 2D
License:	GPLv3
Group:		Games/Adventure
URL:		http://clintbellanger.net/rpg/
Source0:	https://github.com/downloads/clintbellanger/%{name}/%{sname}_%{sversion}.tar.gz
Patch0:		flare-0.15-desktop.patch
BuildRequires:	cmake
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRoot:	%{_tmppath}/%{oname}-%{version}-%{release}

%description
This fantasy dungeon crawl game is a proof of concept implementation of the
Free Libre Action Roleplaying Engine (FLARE). FLARE a simple
isometric-perspective action role-play game engine in the basic style of
Diablo.

%prep
%setup -q -n %{sname}_%{sversion}
%patch0 -p1 -b .desktop

%build
%cmake
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std -C build

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README
%{_gamesbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_gamesdatadir}/%{name}
%{_iconsdir}/hicolor/*/apps/%{name}.*



%changelog
* Tue Dec 27 2011 Andrey Bondrov <abondrov@mandriva.org> 15.1-1mdv2011.0
+ Revision: 745574
- imported package flare

