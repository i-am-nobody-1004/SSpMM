make -f Makefile_volta clean
make -f Makefile_volta spmm_test
make -f Makefile_volta spmm_test_run_cublas
make -f Makefile_volta spmm_test_run_cusparse
make -f Makefile_volta spmm_test_run_sputnik_fp16
make -f Makefile_volta spmm_test_run_vectorsparse
cp ./data/* ../result-data/