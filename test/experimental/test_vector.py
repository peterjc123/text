# -*- coding: utf-8 -*-
import numpy as np
from numpy.testing import assert_allclose
import torch
import torchtext

from test.common.torchtext_test_case import TorchtextTestCase
from torchtext.experimental.vectors import Vectors


class TestVectors(TorchtextTestCase):
    def test_vectors(self):
        tensorA = torch.Tensor([1, 0, 0])
        tensorB = torch.Tensor([0, 1, 0])
        expected_unk_tensor = torch.Tensor([0, 0, 0])
        
        tokens = ['a', 'b']
        vectors = [tensorA, tensorB]
        vectorsObj = Vectors(tokens, vectors)

        self.assertEqual(vectorsObj['empty'].tolist(), expected_unk_tensor.tolist())
        # assert_allclose(vectorsObj['a'].numpy(), tensorA.numpy())
        # assert_allclose(vectorsObj['b'].numpy(), tensorB.numpy())