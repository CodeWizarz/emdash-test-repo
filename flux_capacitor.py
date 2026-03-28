"""
Flux Capacitor Module
Handles temporal displacement field generation with quantum entanglement synchronization.
"""

import time
import threading
from typing import Optional, Dict, Any
from dataclasses import dataclass, field
from enum import Enum
from collections import deque


class FluxState(Enum):
    IDLE = "idle"
    CHARGING = "charging"
    ACTIVE = "active"
    ENGAGED = "engaged"
    ERROR = "error"


class EntanglementStatus(Enum):
    DISENTANGLED = "disentangled"
    PARTIAL = "partial"
    FULL = "full"
    CORRUPTED = "corrupted"


@dataclass
class QuantumState:
    """Represents the quantum state of flux particles."""
    particle_id: str
    spin: float = 0.0
    phase: float = 0.0
    entangled_with: Optional[str] = None
    coherence: float = 1.0
    
    def is_coherent(self) -> bool:
        return self.coherence > 0.7


@dataclass
class FluxCapacitorStatus:
    """Current status of the flux capacitor."""
    state: FluxState = FluxState.IDLE
    entanglement_status: EntanglementStatus = EntanglementStatus.DISENTANGLED
    power_level: float = 0.0
    temporal_offset: float = 0.0
    quantum_coherence: float = 1.0
    error_count: int = 0
    last_error: Optional[str] = None


class QuantumEntanglementManager:
    """
    Manages quantum entanglement between flux particles.
    BUG FIX: Previously had race condition in entanglement state synchronization.
    """
    
    def __init__(self):
        self._states: Dict[str, QuantumState] = {}
        self._entanglement_pairs: Dict[str, str] = {}
        self._lock = threading.RLock()
        self._sync_queue = deque(maxlen=1000)
        
    def add_particle(self, particle_id: str) -> QuantumState:
        with self._lock:
            state = QuantumState(particle_id=particle_id)
            self._states[particle_id] = state
            return state
    
    def entangle_particles(self, particle_a: str, particle_b: str) -> bool:
        """
        Entangle two particles quantum-mechanically.
        
        BUG FIX: Previously did not properly synchronize entanglement state,
        causing quantum decoherence when both particles were accessed simultaneously.
        The fix ensures atomic state updates with proper locking.
        """
        with self._lock:
            if particle_a not in self._states or particle_b not in self._states:
                return False
            
            if particle_a == particle_b:
                return False
            
            # Check if either particle is already entangled
            if self._states[particle_a].entangled_with or self._states[particle_b].entangled_with:
                return False
            
            # Atomic entanglement update - BUG FIX: was not thread-safe before
            self._states[particle_a].entangled_with = particle_b
            self._states[particle_b].entangled_with = particle_a
            
            # Synchronize phases (quantum entanglement requires correlated phases)
            phase_a = self._states[particle_a].phase
            self._states[particle_b].phase = phase_a
            
            self._entanglement_pairs[particle_a] = particle_b
            self._entanglement_pairs[particle_b] = particle_a
            
            # Queue sync event for telemetry
            self._sync_queue.append({
                'event': 'entangle',
                'particles': (particle_a, particle_b),
                'timestamp': time.time()
            })
            
            return True
    
    def disentangle_particles(self, particle_a: str, particle_b: str) -> bool:
        """Disentangle particles with proper state synchronization."""
        with self._lock:
            if particle_a not in self._states or particle_b not in self._states:
                return False
            
            # Verify entanglement exists
            if (self._states[particle_a].entangled_with != particle_b or
                self._states[particle_b].entangled_with != particle_a):
                return False
            
            # Atomic disentanglement - BUG FIX: was causing orphaned entanglement
            self._states[particle_a].entangled_with = None
            self._states[particle_b].entangled_with = None
            
            if particle_a in self._entanglement_pairs:
                del self._entanglement_pairs[particle_a]
            if particle_b in self._entanglement_pairs:
                del self._entanglement_pairs[particle_b]
            
            self._sync_queue.append({
                'event': 'disentangle',
                'particles': (particle_a, particle_b),
                'timestamp': time.time()
            })
            
            return True
    
    def get_entanglement_status(self, particle_id: str) -> EntanglementStatus:
        """Get the entanglement status of a particle."""
        with self._lock:
            if particle_id not in self._states:
                return EntanglementStatus.DISENTANGLED
            
            state = self._states[particle_id]
            
            if state.entangled_with is None:
                return EntanglementStatus.DISENTANGLED
            
            # Check coherence
            if not state.is_coherent():
                return EntanglementStatus.CORRUPTED
            
            # Check if entangled particle exists and is coherent
            entangled_id = state.entangled_with
            if entangled_id in self._states:
                entangled_state = self._states[entangled_id]
                if entangled_state.is_coherent():
                    return EntanglementStatus.FULL
                return EntanglementStatus.PARTIAL
            
            return EntanglementStatus.CORRUPTED
    
    def synchronize_entanglement(self) -> bool:
        """
        Synchronize all entanglement states.
        
        BUG FIX: This method was missing entirely, causing quantum states
        to become desynchronized over time, leading to temporal paradoxes.
        """
        with self._lock:
            synchronized = 0
            errors = 0
            
            for particle_id, state in self._states.items():
                if state.entangled_with:
                    entangled_id = state.entangled_with
                    if entangled_id in self._states:
                        entangled_state = self._states[entangled_id]
                        
                        # Ensure bidirectional entanglement is consistent
                        if entangled_state.entangled_with != particle_id:
                            # Fix corrupted entanglement
                            entangled_state.entangled_with = particle_id
                            errors += 1
                        
                        # Synchronize phases (quantum correlation)
                        avg_phase = (state.phase + entangled_state.phase) / 2
                        state.phase = avg_phase
                        entangled_state.phase = avg_phase
                        
                        # Synchronize coherence
                        avg_coherence = (state.coherence + entangled_state.coherence) / 2
                        state.coherence = avg_coherence
                        entangled_state.coherence = avg_coherence
                        
                        synchronized += 1
            
            return errors == 0


class FluxCapacitor:
    """
    Flux Capacitor for temporal displacement.
    
    BUG FIX: Fixed quantum entanglement synchronization bug that was causing
    temporal field instability during 88 mph engagement events.
    """
    
    def __init__(self):
        self._status = FluxCapacitorStatus()
        self._quantum_manager = QuantumEntanglementManager()
        self._particles = []
        self._target_speed = 88.0  # mph
        self._lock = threading.Lock()
        
        # Initialize quantum particles
        self._initialize_particles()
    
    def _initialize_particles(self):
        """Initialize the three required flux particles."""
        particle_ids = ['flux_alpha', 'flux_beta', 'flux_gamma']
        for pid in particle_ids:
            self._quantum_manager.add_particle(pid)
            self._particles.append(pid)
        
        # Entangle all particles for maximum quantum coherence
        self._quantum_manager.entangle_particles('flux_alpha', 'flux_beta')
        self._quantum_manager.entangle_particles('flux_beta', 'flux_gamma')
        self._quantum_manager.entangle_particles('flux_gamma', 'flux_alpha')
    
    @property
    def status(self) -> FluxCapacitorStatus:
        return self._status
    
    def charge(self, power_level: float) -> bool:
        """
        Charge the flux capacitor to the specified power level.
        
        BUG FIX: Added quantum entanglement synchronization during charging
        to prevent coherence loss at high power levels.
        """
        with self._lock:
            if self._status.state == FluxState.ENGAGED:
                return False
            
            self._status.state = FluxState.CHARGING
            self._status.power_level = min(power_level, 100.0)
            
            # BUG FIX: Synchronize entanglement during charging
            # Previously this was missing, causing quantum decoherence
            sync_success = self._quantum_manager.synchronize_entanglement()
            
            if not sync_success:
                self._status.error_count += 1
                self._status.last_error = "Quantum synchronization failed during charge"
                self._status.state = FluxState.ERROR
                return False
            
            # Update coherence based on entanglement status
            coherence_sum = 0.0
            for pid in self._particles:
                status = self._quantum_manager.get_entanglement_status(pid)
                if status == EntanglementStatus.FULL:
                    coherence_sum += 1.0
                elif status == EntanglementStatus.PARTIAL:
                    coherence_sum += 0.5
                elif status == EntanglementStatus.CORRUPTED:
                    coherence_sum += 0.0
            
            self._status.quantum_coherence = coherence_sum / len(self._particles)
            
            if self._status.quantum_coherence < 0.5:
                self._status.error_count += 1
                self._status.last_error = "Insufficient quantum coherence"
                self._status.state = FluxState.ERROR
                return False
            
            return True
    
    def engage(self, vehicle_speed: float) -> bool:
        """
        Engage the flux capacitor at the specified vehicle speed.
        
        BUG FIX: Fixed race condition where quantum entanglement state
        could become corrupted during rapid speed changes, causing
        the capacitor to engage at incorrect temporal coordinates.
        """
        with self._lock:
            if self._status.state == FluxState.ENGAGED:
                return True
            
            if vehicle_speed < self._target_speed:
                self._status.state = FluxState.IDLE
                return False
            
            # BUG FIX: Critical synchronization before engagement
            # This was the source of the "quantum entanglement bug"
            sync_success = self._quantum_manager.synchronize_entanglement()
            
            if not sync_success:
                self._status.error_count += 1
                self._status.last_error = "Pre-engagement quantum sync failed"
                self._status.state = FluxState.ERROR
                return False
            
            # Verify all particles are fully entangled
            for pid in self._particles:
                status = self._quantum_manager.get_entanglement_status(pid)
                if status != EntanglementStatus.FULL:
                    self._status.error_count += 1
                    self._status.last_error = f"Particle {pid} not fully entangled"
                    self._status.state = FluxState.ERROR
                    return False
            
            # Calculate temporal offset based on power and speed
            power_factor = self._status.power_level / 100.0
            speed_factor = vehicle_speed / self._target_speed
            self._status.temporal_offset = power_factor * speed_factor * 30.0  # years
            
            self._status.state = FluxState.ENGAGED
            return True
    
    def disengage(self) -> bool:
        """Disengage the flux capacitor."""
        with self._lock:
            self._status.state = FluxState.IDLE
            self._status.temporal_offset = 0.0
            return True
    
    def reset(self) -> bool:
        """
        Reset the flux capacitor to initial state.
        
        BUG FIX: Added full quantum state reset to clear any corrupted
        entanglement states that may have accumulated.
        """
        with self._lock:
            # Disentangle all particles
            for i, pid in enumerate(self._particles):
                for j, other_pid in enumerate(self._particles):
                    if i != j:
                        self._quantum_manager.disentangle_particles(pid, other_pid)
            
            # Re-entangle with fresh state
            self._quantum_manager.entangle_particles('flux_alpha', 'flux_beta')
            self._quantum_manager.entangle_particles('flux_beta', 'flux_gamma')
            self._quantum_manager.entangle_particles('flux_gamma', 'flux_alpha')
            
            # Synchronize to ensure clean state
            self._quantum_manager.synchronize_entanglement()
            
            self._status = FluxCapacitorStatus()
            return True


# Module-level instance
_capacitor: Optional[FluxCapacitor] = None


def get_flux_capacitor() -> FluxCapacitor:
    """Get the global flux capacitor instance."""
    global _capacitor
    if _capacitor is None:
        _capacitor = FluxCapacitor()
    return _capacitor
