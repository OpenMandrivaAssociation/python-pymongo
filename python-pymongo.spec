%define module pymongo

Name:	python-pymongo
Version:	4.17.0
Release:	1
Summary:	The Official MongoDB Python driver
Group:		Development/Python
License:	Apache-2.0
URL:		https://pymongo.readthedocs.io/en/stable/
Source0:	https://github.com/mongodb/mongo-python-driver/archive/%{version}/%{name}-%{version}.tar.gz
# repo - https://github.com/mongodb/mongo-python-driver
Source100:	%{name}.rpmlintrc

BuildSystem:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(dnspython)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatch-requirements-txt)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	python%{pyver}dist(bson) = %{EVRD}
Recommends:	python%{pyver}dist(certifi)
Recommends:	python%{pyver}dist(cryptography)
Recommends:	python%{pyver}dist(pyopenssl)
Recommends:	python%{pyver}dist(requests)
Recommends:	python%{pyver}dist(service-identity)

%description
The PyMongo distribution contains tools for interacting with MongoDB
database from Python.

The bson package is an implementation of the BSON format for Python.
The pymongo package is a native Python driver for MongoDB.
The gridfs package is a gridfs implementation on top of pymongo.
This driver is build without the C extensions.

%package -n python-bson
License:	Apache-2.0 AND MIT
Summary:	Python bson library
Group:		Development/Python
Provides:	python%{pyver}dist(bson) = %{EVRD}

%description -n python-bson
BSON is a binary-encoded serialization of JSON-like documents. BSON is designed
to be lightweight, traversable, and efficient. BSON, like JSON, supports the
embedding of objects and arrays within other objects and arrays.

%package -n python-gridfs
License:	Apache-2.0
Summary:	Python GridFS driver for MongoDB
Group:		Development/Python
Provides:	python%{pyver}dist(gridfs) = %{EVRD}
Requires:	python-pymongo = %{EVRD}

%description -n python-gridfs
GridFS is a storage specification for large objects in MongoDB.

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"
export PYMONGO_C_EXT_MUST_BUILD=1

%files
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info

%files -n python-bson
%license LICENSE
%doc README.md
%{python_sitearch}/bson

%files -n python-gridfs
%license LICENSE
%doc README.md
%{python_sitearch}/gridfs
