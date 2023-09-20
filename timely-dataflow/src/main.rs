extern crate timely;

use timely::dataflow::operators::{ToStream, Map, Inspect};

fn main() {
    timely::execute_from_args(std::env::args(), |worker| {
        worker.dataflow::<(),_,_>(|scope| {
            (0..10)
            .to_stream(scope)
            .map(|x| x + 1)
            .inspect(|x| println!("hello {}!", x));
        });
    }).unwrap();
}
