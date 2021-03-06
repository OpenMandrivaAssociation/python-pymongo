%define shortname    pymongo

Name:           python-%{shortname}
Version:	3.8.0
Release:	1
Summary:        Python driver for MongoDB


Group:          Development/Python
License:        Apache License
URL:            http://api.mongodb.org/python/2.1/
Source0:	https://files.pythonhosted.org/packages/19/77/da358f5729ff046ceaf6c6a86755f9d8285719f93df6da15bb2440367d7e/pymongo-3.8.0.tar.gz
BuildRequires:  python-setuptools
BuildRequires:  python-devel

%define debug_package %{nil}

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
python setup.py --no_ext build

%install
python setup.py --no_ext install -O1 --skip-build --root %{buildroot} --install-purelib=%{py_platsitedir}

%files
%{py_platsitedir}/*



