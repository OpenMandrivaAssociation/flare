Name:		flare
Version:	1.13
Release:	1
Summary:	Diablo-like role-playing game in 2D
License:	GPLv3
Group:		Games/Adventure
URL:		http://flarerpg.org/
Source0:	https://github.com/flareteam/flare-engine/archive/v%{version}/%{name}-engine-%{version}.tar.gz
Source1:  https://github.com/flareteam/flare-game/archive/v%{version}/%{name}-game-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(SDL2_mixer)
BuildRequires:	pkgconfig(SDL2_image)
BuildRequires:	pkgconfig(SDL2_ttf)

#BuildRoot:	%{_tmppath}/%{oname}-%{version}-%{release}

%description
This fantasy dungeon crawl game is a proof of concept implementation of the
Free Libre Action Roleplaying Engine (FLARE). FLARE a simple
isometric-perspective action role-play game engine in the basic style of
Diablo.

%prep
%setup -qn %{name}-engine-%{version} -b1

%build
pushd ../%{name}-game-%{version}
%cmake
%make_build
popd

%cmake
%make_build

%install
%make_install -C build
%make_install -C ../%{name}-game-%{version}/build
sed -i -e 's/RolePlaying/AdventureGame/' -e '/TryExec/d' %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc README.engine.md CREDITS.engine.txt ../%{name}-game-%{version}/{README,CREDITS.txt}
%{_gamesbindir}/%{name}
%{_datadir}/metainfo/org.flarerpg.Flare.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
%{_mandir}/man6/flare.6.*
%{_gamesdatadir}/%{name}
