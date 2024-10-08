import os
os.environ['CUDA_HOME'] = '/usr/local/cuda-11.8'
from setuptools import setup
from torch.utils.cpp_extension import CppExtension, BuildExtension, CUDAExtension

setup(
    name='sptrans',
    version='0.0.2',
    description='Custom library for Sparse Transformer for pytorch',
    author='nobody',
    author_email='xxxx',
    ext_modules=[
        CUDAExtension('sptrans.sddmm', 
                      ['cuda/sddmm.cpp', 'cuda/sddmm_kernel.cu'],
                      extra_compile_args={'cxx':[], 'nvcc':['-arch=sm_89', '-lcusparse', '--ptxas-options=-v', '-lineinfo']}),
        CUDAExtension('sptrans.spmm', 
                      ['cuda/spmm.cpp', 'cuda/spmm_kernel.cu'],
                      extra_compile_args={'cxx':[], 'nvcc':['-arch=sm_89', '-lcusparse', '--ptxas-options=-v', '-lineinfo']}),
        CUDAExtension('sptrans.softmax', 
                      ['cuda/softmax.cpp', 'cuda/softmax_kernel.cu'],
                      extra_compile_args={'cxx':[], 'nvcc':['-arch=sm_89', '-lcusparse', '--ptxas-options=-v', '-lineinfo']}),
        ],
    cmdclass={'build_ext': BuildExtension},
    install_requires=['torch']
)
