import FWCore.ParameterSet.Config as cms

from ..modules.hltL3fL1TkSingleMu22L3Filtered50Q_cfi import *
from ..modules.hltPhase2L3MuonCandidates_cfi import *
from ..modules.hltPhase2PixelFitterByHelixProjections_cfi import *
from ..modules.hltPhase2PixelTrackFilterByKinematics_cfi import *
from ..sequences.HLTBeginSequence_cfi import *
from ..sequences.HLTEndSequence_cfi import *
from ..sequences.HLTMuonsSequence_cfi import *
from ..sequences.HLTTrackingV61Sequence_cfi import *
from ..sequences.itLocalRecoSequence_cfi import *
from ..sequences.muonlocalrecoSequence_cfi import *
from ..sequences.otLocalRecoSequence_cfi import *

HLT_Mu50_FromL1TkMuon = cms.Path(HLTBeginSequence+muonlocalrecoSequence+itLocalRecoSequence+otLocalRecoSequence+hltPhase2PixelFitterByHelixProjections+hltPhase2PixelTrackFilterByKinematics+HLTTrackingV61Sequence+HLTMuonsSequence+hltPhase2L3MuonCandidates+hltL3fL1TkSingleMu22L3Filtered50Q+HLTEndSequence)
