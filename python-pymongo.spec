%define shortname    pymongo

Name:           python-%{shortname}
Version:        1.11
Release:        %mkrel 1
Summary:        Python driver for MongoDB
Group:          Development/Python
License:        Apache License
URL:            http://api.mongodb.org/python/1.11
Source0:        http://pypi.python.org/packages/source/p/pymongo/%{shortname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  python-setuptools
%py_requires -d

%description
The PyMongo distribution contains tools for interacting with MongoDB
database from Python.

The bson package is an implementation of the BSON format for Python.

The pymongo package is a native Python driver for MongoDB.

The gridfs package is a gridfs implementation on top of pymongo.

This driver is build without the C extensions.

%prep
%setup -q -n %{shortname}-%{version}

%build
%{__python} setup.py --no_ext build

%install
rm -rf %{buildroot}
%{__python} setup.py --no_ext install -O1 --skip-build --root %{buildroot} --install-purelib=%py_platsitedir

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{py_platsitedir}/*
