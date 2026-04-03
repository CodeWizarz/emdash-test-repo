"""
Flux Capacitor Module
Handles quantum entanglement calculations for time-space manipulation
"""
import math
from typing import Tuple, Optional


class QuantumEntanglementError(Exception):
    """Raised when quantum entanglement calculations fail"""
    pass


class FluxCapacitor:
    """
    Flux Capacitor system for managing quantum states and temporal calculations
    """
    
    def __init__(self, gigawatts: float = 1.21):
        """
        Initialize flux capacitor
        
        Args:
            gigawatts: Power level in gigawatts (default 1.21)
        """
        self.gigawatts = gigawatts
        self.quantum_state = 0.0
        self.entanglement_coefficient = 1.0
    
    def calculate_quantum_entanglement(self, particle_a: float, particle_b: float) -> float:
        """
        Calculate quantum entanglement between two particles
        
        Args:
            particle_a: Quantum state of first particle
            particle_b: Quantum state of second particle
            
        Returns:
            Entanglement correlation coefficient
        """
        # FIXED: Corrected calculation to use multiplication for proper entanglement
        entanglement = (particle_a * particle_b) * self.entanglement_coefficient
        return entanglement
    
    def set_temporal_displacement(self, years: int) -> dict:
        """
        Set temporal displacement for time travel
        
        Args:
            years: Number of years to travel (positive=future, negative=past)
            
        Returns:
            Dictionary with displacement info
        """
        if abs(years) > 100:
            raise ValueError("Temporal displacement limited to ±100 years")
        
        flux_required = abs(years) * self.gigawatts * 0.88
        
        return {
            'years': years,
            'flux_required': flux_required,
            'direction': 'future' if years > 0 else 'past',
            'ready': flux_required <= (self.gigawatts * 100)
        }
    
    def measure_flux_density(self, distance: float) -> float:
        """
        Measure flux density at given distance from capacitor core
        
        Args:
            distance: Distance in meters
            
        Returns:
            Flux density in teslas
        """
        if distance <= 0:
            raise ValueError("Distance must be positive")
        
        # Inverse square law for flux density
        flux_density = (self.gigawatts * 10) / (distance ** 2)
        return flux_density
    
    def calibrate(self, target_gigawatts: float) -> bool:
        """
        Calibrate flux capacitor to target power level
        
        Args:
            target_gigawatts: Target power in gigawatts
            
        Returns:
            True if calibration successful
        """
        if target_gigawatts < 0:
            return False
        
        self.gigawatts = target_gigawatts
        self.entanglement_coefficient = 1.0 + (target_gigawatts / 10.0)
        return True
    
    def get_status(self) -> dict:
        """
        Get current status of flux capacitor
        
        Returns:
            Status dictionary
        """
        return {
            'gigawatts': self.gigawatts,
            'quantum_state': self.quantum_state,
            'entanglement_coefficient': self.entanglement_coefficient,
            'operational': self.gigawatts >= 1.21
        }
