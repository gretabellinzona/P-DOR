from setuptools import setup

setup(
    name='P-DOR',
    version='0.1.0',
    description='a Pipeline to Disentangle Outbreaks Rapidly',
    author='Gherard Batisti Biffignandi, Greta Bellinzona, Greta Petazzoni, Stefano Gaiarsa',
    url='https://github.com/gretabellinzona/P-DOR',
    packages=['P-DOR'],
    install_requires=[
        '_libgcc_mutex==0.1',
        '_openmp_mutex==4.5',
        '_r-mutex==1.0.1',
        'assembly-stats==1.0.1',
        'binutils_impl_linux-64==2.39',
        'bioconductor-ggtree==3.6.0',
        'bioconductor-ggtreeextra==1.8.0',
        'bioconductor-treeio==1.22.0',
        'biopython==1.80',
        'blast==2.13.0',
        'bwidget==1.9.14',
        'bzip2==1.0.8',
        'c-ares==1.18.1',
        'ca-certificates==2022.12.7',
        'cairo==1.16.0',
        'curl==7.87.0',
        'entrez-direct==16.2',
        'expat==2.5.0',
        'font-ttf-dejavu-sans-mono==2.37',
        'font-ttf-inconsolata==3.000',
        'font-ttf-source-code-pro==2.038',
        'font-ttf-ubuntu==0.83',
        'fontconfig==2.14.1',
        'fonts-conda-ecosystem==1',
        'fonts-conda-forge==1',
        'freetype==2.12.1',
        'fribidi==1.0.10',
        'gcc_impl_linux-64==12.2.0',
        'gettext==0.21.1',
        'gfortran_impl_linux-64==12.2.0',
        'glpk==5.0',
        'gmp==6.2.1',
        'graphite2==1.3.13',
        'gsl==2.7',
        'gxx_impl_linux-64==12.2.0',
        'harfbuzz==6.0.0',
        'hmmer==3.3.2',
        'icu==70.1',
        'iqtree==2.2.0.3',
        'jpeg==9e',
        'kernel-headers_linux-64==2.6.32',
        'keyutils==1.6.1',
        'krb5==1.20.1',
        'ld_impl_linux-64==2.39',
        'lerc==4.0.0',
        'libblas==3.9.0',
        'libcblas==3.9.0',
        'libcurl==7.87.0',
        'libdeflate==1.17',
        'libedit==3.1.20191231',
        'libev==4.33',
        'libffi==3.4.2',
        'libgcc==7.2.0',
        'libgcc-devel_linux-64==12.2.0',
        'libgcc-ng==12.2.0',
        'libgfortran-ng==12.2.0',
        'libgfortran5==12.2.0',
        'libglib==2.74.1',
        'libgomp==12.2.0',
        'libiconv==1.17',
        'libidn2==2.3.4',
        'liblapack==3.9.0',
        'libnghttp2==1.51.0',
        'libnsl==2.0.0',
        'libopenblas==0.3.21',
        'libpng==1.6.39',
        'libsanitizer==12.2.0',
        'libsqlite==3.40.0',
        'libssh2==1.10.0',
        'libstdcxx-devel_linux-64==12.2.0',
        'libstdcxx-ng==12.2.0',
        'libtiff==4.5.0',
        'libunistring==0.9.10',
        'libuuid==2.32.1',
        'libwebp-base==1.2.4',
        'libxcb==1.13',
        'libxml2==2.10.3',
        'libzlib==1.2.13',
        'make==4.3',
        'mash==1.1',
        'mummer4==4.0.0rc1',
        'ncbi-amrfinderplus==3.11.2',
        'ncurses==6.3',
        'numpy==1.24.1',
        'openssl==3.0.7',
        'pandas==1.5.3',
        'pango==1.50.12',
        'parallel==20230122',
        'pcre==8.45',
        'pcre2==10.40',
        'perl==5.32.1',
        'perl-archive-tar==2.40',
        'perl-carp==1.38',
        'perl-common-sense==3.75',
        'perl-compress-raw-bzip2==2.201',
        'perl-compress-raw-zlib==2.105',
        'perl-encode==3.19',
        'perl-exporter==5.72',
        'perl-exporter-tiny==1.002002',
        'perl-extutils-makemaker==7.66',
        'perl-io-compress==2.201',
        'perl-io-zlib==1.14',
        'perl-json==4.10',
        'perl-json-xs==2.34',
        'perl-list-moreutils==0.430',
        'perl-list-moreutils-xs==0.430',
        'perl-parent==0.236',
        'perl-pathtools==3.75',
        'perl-scalar-list-utils==1.62',
        'perl-types-serialiser==1.01',
        'pip==22.3.1',
        'pixman==0.40.0',
        'pthread-stubs==0.4',
        'python==3.8.15',
        'python-dateutil==2.8.2',
        'python_abi==3.8',
        'pytz==2022.7.1',
        'r-ape==5.6_2',
        'r-aplot==0.1.9',
        'r-base==4.2.2',
        'r-cli==3.3.0',
        'r-colorspace==2.0_3',
        'r-cpp11==0.4.2',
        'r-crayon==1.5.1',
        'r-digest==0.6.29',
        'r-dplyr==1.0.9',
        'r-ellipsis==0.3.2',
        'r-fansi==1.0.3',
        'r-farver==2.1.0',
        'r-generics==0.1.2',
        'r-ggfun==0.0.9',
        'r-ggnewscale==0.4.8',
        'r-ggplot2==3.3.6',
        'r-ggplotify==0.1.0',
        'r-glue==1.6.2',
        'r-gridgraphics==0.5_1',
        'r-gtable==0.3.0',
        'r-igraph==1.3.5',
        'r-isoband==0.2.5',
        'r-jsonlite==1.8.0',
        'r-labeling==0.4.2',
        'r-lattice==0.20_45',
        'r-lazyeval==0.2.2',
        'r-lifecycle==1.0.1',
        'r-magrittr==2.0.3',
        'r-mass==7.3_57',
        'r-matrix==1.4_1',
        'r-mgcv==1.8_40',
        'r-munsell==0.5.0',
        'r-nlme==3.1_157',
        'r-patchwork==1.1.1',
        'r-pheatmap==1.0.12',
        'r-pillar==1.7.0',
        'r-pkgconfig==2.0.3',
        'r-plyr==1.8.8',
        'r-purrr==0.3.4',
        'r-r6==2.5.1',
        'r-rcolorbrewer==1.1_3',
        'r-rcpp==1.0.8.3',
        'r-reshape2==1.4.4',
        'r-rlang==1.0.2',
        'r-scales==1.2.0',
        'r-stringi==1.7.12',
        'r-stringr==1.4.0',
        'r-svglite==2.1.1',
        'r-systemfonts==1.0.4',
        'r-tibble==3.1.7',
        'r-tidyr==1.2.0',
        'r-tidyselect==1.1.2',
        'r-tidytree==0.4.2',
        'r-utf8==1.2.2',
        'r-vctrs==0.4.1',
        'r-viridislite==0.4.0',
        'r-withr==2.5.0',
        'r-yulab.utils==0.0.4',
        'readline==8.1.2',
        'sed==4.8',
        'setuptools==66.1.1',
        'six==1.16.0',
        'sysroot_linux-64==2.12',
        'tk==8.6.12',
        'tktable==2.10',
        'wget==1.20.3',
        'wheel==0.38.4',
        'xorg-kbproto==1.0.7',
        'xorg-libice==1.0.10',
        'xorg-libsm==1.2.3',
        'xorg-libx11==1.7.2',
        'xorg-libxau==1.0.9',
        'xorg-libxdmcp==1.1.3',
        'xorg-libxext==1.3.4',
        'xorg-libxrender==0.9.10',
        'xorg-libxt==1.2.1',
        'xorg-renderproto==0.11.1',
        'xorg-xextproto==7.3.0',
        'xorg-xproto==7.0.31',
        'xz==5.2.6',
        'zlib==1.2.13',
        'zstd==1.5.2',
    ],
)
