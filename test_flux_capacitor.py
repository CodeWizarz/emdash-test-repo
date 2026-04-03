"""
Tests for Flux Capacitor Module
Verifies quantum entanglement calculations and temporal functions
"""
import pytest
import math
from flux_capacitor import FluxCapacitor, QuantumEntanglementError


class TestFluxCapacitorInitialization:
    """Test flux capacitor initialization"""
    
    def test_default_initialization(self):
        """Test default initialization with 1.21 gigawatts"""
        fc = FluxCapacitor()
        assert fc.gigawatts == 1.21
        assert fc.quantum_state == 0.0
        assert fc.entanglement_coefficient == 1.0
    
    def test_custom_gigawatts(self):
        """Test initialization with custom gigawatts"""
        fc = FluxCapacitor(gigawatts=2.5)
        assert fc.gigawatts == 2.5


class TestQuantumEntanglement:
    """Test quantum entanglement calculations - verifies bug fix"""
    
    def test_positive_particles_entanglement(self):
        """Test entanglement with positive particle states"""
        fc = FluxCapacitor()
        result = fc.calculate_quantum_entanglement(2.0, 3.0)
        # With multiplication fix: 2.0 * 3.0 * 1.0 = 6.0
        assert result == 6.0
    
    def test_negative_particles_entanglement(self):
        """Test entanglement with negative particle states"""
        fc = FluxCapacitor()
        result = fc.calculate_quantum_entanglement(-2.0, 3.0)
        # -2.0 * 3.0 * 1.0 = -6.0
        assert result == -6.0
    
    def test_zero_particle_entanglement(self):
        """Test entanglement when one particle is zero"""
        fc = FluxCapacitor()
        result = fc.calculate_quantum_entanglement(0.0, 5.0)
        assert result == 0.0
    
    def test_entanglement_with_coefficient(self):
        """Test entanglement respects coefficient"""
        fc = FluxCapacitor()
        fc.entanglement_coefficient = 2.0
        result = fc.calculate_quantum_entanglement(3.0, 4.0)
        # 3.0 * 4.0 * 2.0 = 24.0
        assert result == 24.0
    
    def test_symmetric_entanglement(self):
        """Test that entanglement is symmetric (particle order doesn't matter)"""
        fc = FluxCapacitor()
        result1 = fc.calculate_quantum_entanglement(5.0, 7.0)
        result2 = fc.calculate_quantum_entanglement(7.0, 5.0)
        assert result1 == result2
    
    def test_identical_particles(self):
        """Test entanglement of identical particles"""
        fc = FluxCapacitor()
        result = fc.calculate_quantum_entanglement(4.0, 4.0)
        # 4.0 * 4.0 * 1.0 = 16.0
        assert result == 16.0


class TestTemporalDisplacement:
    """Test temporal displacement calculations"""
    
    def test_future_displacement(self):
        """Test displacement to future"""
        fc = FluxCapacitor()
        result = fc.set_temporal_displacement(10)
        assert result['years'] == 10
        assert result['direction'] == 'future'
        assert result['flux_required'] == pytest.approx(10 * 1.21 * 0.88)
        assert result['ready'] is True
    
    def test_past_displacement(self):
        """Test displacement to past"""
        fc = FluxCapacitor()
        result = fc.set_temporal_displacement(-25)
        assert result['years'] == -25
        assert result['direction'] == 'past'
        assert result['flux_required'] == pytest.approx(25 * 1.21 * 0.88)
    
    def test_displacement_limit_exceeded(self):
        """Test that displacement beyond ±100 years raises error"""
        fc = FluxCapacitor()
        with pytest.raises(ValueError, match="Temporal displacement limited"):
            fc.set_temporal_displacement(150)
    
    def test_zero_displacement(self):
        """Test zero displacement (staying in present)"""
        fc = FluxCapacitor()
        result = fc.set_temporal_displacement(0)
        assert result['years'] == 0
        assert result['flux_required'] == 0


class TestFluxDensity:
    """Test flux density measurements"""
    
    def test_flux_density_at_1_meter(self):
        """Test flux density at 1 meter"""
        fc = FluxCapacitor()
        density = fc.measure_flux_density(1.0)
        assert density == pytest.approx(1.21 * 10)
    
    def test_flux_density_inverse_square(self):
        """Test inverse square law for flux density"""
        fc = FluxCapacitor()
        density_1m = fc.measure_flux_density(1.0)
        density_2m = fc.measure_flux_density(2.0)
        # At 2m, density should be 1/4 of density at 1m
        assert density_2m == pytest.approx(density_1m / 4)
    
    def test_flux_density_invalid_distance(self):
        """Test that zero or negative distance raises error"""
        fc = FluxCapacitor()
        with pytest.raises(ValueError, match="Distance must be positive"):
            fc.measure_flux_density(0)
        with pytest.raises(ValueError, match="Distance must be positive"):
            fc.measure_flux_density(-5.0)


class TestCalibration:
    """Test flux capacitor calibration"""
    
    def test_calibration_increases_power(self):
        """Test calibration to higher power level"""
        fc = FluxCapacitor()
        result = fc.calibrate(5.0)
        assert result is True
        assert fc.gigawatts == 5.0
        assert fc.entanglement_coefficient == pytest.approx(1.0 + 5.0/10.0)
    
    def test_calibration_decreases_power(self):
        """Test calibration to lower power level"""
        fc = FluxCapacitor(gigawatts=10.0)
        result = fc.calibrate(2.0)
        assert result is True
        assert fc.gigawatts == 2.0
    
    def test_calibration_negative_fails(self):
        """Test that negative calibration fails"""
        fc = FluxCapacitor()
        result = fc.calibrate(-1.0)
        assert result is False
        assert fc.gigawatts == 1.21  # unchanged


class TestStatus:
    """Test status reporting"""
    
    def test_status_includes_all_fields(self):
        """Test that status includes all expected fields"""
        fc = FluxCapacitor()
        status = fc.get_status()
        assert 'gigawatts' in status
        assert 'quantum_state' in status
        assert 'entanglement_coefficient' in status
        assert 'operational' in status
    
    def test_operational_when_sufficient_power(self):
        """Test operational flag when power is sufficient"""
        fc = FluxCapacitor(gigawatts=1.21)
        status = fc.get_status()
        assert status['operational'] is True
    
    def test_not_operational_when_insufficient_power(self):
        """Test operational flag when power is insufficient"""
        fc = FluxCapacitor(gigawatts=0.5)
        status = fc.get_status()
        assert status['operational'] is False


class TestIntegration:
    """Integration tests for complete workflows"""
    
    def test_calibrate_and_calculate_entanglement(self):
        """Test calibration affects entanglement calculations"""
        fc = FluxCapacitor()
        fc.calibrate(5.0)
        
        # Entanglement coefficient should be 1.0 + 5.0/10.0 = 1.5
        result = fc.calculate_quantum_entanglement(2.0, 3.0)
        assert result == pytest.approx(2.0 * 3.0 * 1.5)
    
    def test_full_temporal_journey(self):
        """Test complete temporal displacement scenario"""
        fc = FluxCapacitor(gigawatts=1.21)
        
        # Set displacement to 1985
        future = fc.set_temporal_displacement(30)
        assert future['ready'] is True
        
        # Return to present
        present = fc.set_temporal_displacement(0)
        assert present['flux_required'] == 0


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
