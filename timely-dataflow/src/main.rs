extern crate timely;

use timely::dataflow::operators::{ToStream, Map, Inspect, Operator};
use timely::dataflow::channels::pact::Pipeline;

fn main() {
    timely::example(|scope| {
        (0..10)
        .to_stream(scope)
        .unary(Pipeline, "increment", |capability, info| {
            let mut vector = Vec::new();

            move |input, output| {
                while let Some((time, data)) = input.next() {
                    data.swap(&mut vector);
                    let mut session = output.session(&time);
                    for datum in vector.drain(..) {
                        session.give(datum + 1);
                    }
                }
            }
        });
    })
}
