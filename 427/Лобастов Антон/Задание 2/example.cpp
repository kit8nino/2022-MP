#include <array>
#include "signal.hpp"

typedef std::array<signal::type&, 4> signal_types;

int main() {
    signal_types type = {signal::harmonic{}, signal::triangle{}, signal::PWM{2}, signal::saw{}};
    int period = 2, sampling = 100, amplitude = 3;

    signal::generate::simple ssg = {type[1], period, sampling, amplitude, signal::duration::seconds{5, sampling}};

    signal::generate::amplitude_modular amg = {type[1], period, sampling, amplitude, signal::duration::seconds{5, sampling}, signal::sequence{}};

    signal::sequence sig = ssg.generate(signal::duration::samples(12000));
    signal::sample samp = ssg.generate.next();

    signal::analyzer analyze{sig};

    analyze.plot();
    analyze.fourier_plot();
    analyze.reverse_fourier_plot();
    analyze.disperse();
    analyze.median();
    analyze.mean();
    analyze.max();
    analyze.min();
    analyze.span();

    chain ch{sig};
    
    ch.bypass();
    ch.Butterworth();
    ch(signal::duration::seconds{5, sampling});
    ch.next();
    ch.push(samp);
    ch.push(sig);

    return 0;
}