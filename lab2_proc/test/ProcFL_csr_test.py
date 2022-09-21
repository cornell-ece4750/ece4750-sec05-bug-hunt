#=========================================================================
# ProcFL_csr_test.py
#=========================================================================

import pytest

from pymtl3 import *
from .harness import *
from lab2_proc.ProcFL import ProcFL

#-------------------------------------------------------------------------
# csr
#-------------------------------------------------------------------------

from . import inst_csr

@pytest.mark.parametrize( "name,test", [
  asm_test( inst_csr.gen_basic_test      ),
  asm_test( inst_csr.gen_bypass_test     ),
  asm_test( inst_csr.gen_value_test      ),
  asm_test( inst_csr.gen_random_test     ),
  asm_test( inst_csr.gen_core_stats_test ),
])
def test_csr( name, test ):
  run_test( ProcFL, test )
