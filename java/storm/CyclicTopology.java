	

    package storm.experiment;
     
    import java.util.ArrayList;
    import java.util.List;
    import java.util.Map;
    import java.util.logging.Logger;
     
    import backtype.storm.Config;
    import backtype.storm.LocalCluster;
    import backtype.storm.generated.StormTopology;
    import backtype.storm.spout.SpoutOutputCollector;
    import backtype.storm.task.OutputCollector;
    import backtype.storm.task.TopologyContext;
    import backtype.storm.topology.OutputFieldsDeclarer;
    import backtype.storm.topology.TopologyBuilder;
    import backtype.storm.topology.base.BaseRichBolt;
    import backtype.storm.topology.base.BaseRichSpout;
    import backtype.storm.tuple.Fields;
    import backtype.storm.tuple.Tuple;
    import backtype.storm.tuple.Values;
     
    public class CyclicTopology {
     
            public static final String fountainStream = "fountainStream";
            public static final String gullyStream = "gullyStream";
     
            private static class WaterSpout extends BaseRichSpout {
     
     
                    private static final long serialVersionUID = -992077936760898653L;
                    private SpoutOutputCollector _collector;
     
                    long drop = 0;
     
                    @SuppressWarnings("rawtypes")
                    @Override
                    public void open(Map conf, TopologyContext context,
                                    SpoutOutputCollector collector) {
                            _collector = collector;
     
                    }
     
                    @Override
                    public void nextTuple() {
                            _collector.emit(new Values("drop "+ drop++));
                    }
     
                    @Override
                    public void declareOutputFields(OutputFieldsDeclarer declarer) {
                            declarer.declare(new Fields("drop"));
                    }
     
            }
     
            private static class FountainBolt extends BaseRichBolt {
     
                    private static final long serialVersionUID = -5232340252708532106L;
                    private OutputCollector _collector;
     
     
     
                    @SuppressWarnings("rawtypes")
                    @Override
                    public void prepare(Map stormConf, TopologyContext context,
                                    OutputCollector collector) {
                            _collector = collector;
     
                    }
     
                    @Override
                    public void execute(Tuple input) {
                            if (input.size() == 1) {
                                    String drop = input.getString(0);
                                    List<Object> output = new ArrayList<Object>(2);
                                    output.add(drop);
                                    output.add(1);
                                    _collector.emit(fountainStream, input, output);
                            } else if (input.size() == 2) {
                                    String drop = input.getString(0);
                                    Integer count = input.getInteger(1);
     
                                    List<Object> output = new ArrayList<Object>(2);
     
                                    if (count < 3) {
                                            output.add(drop);
                                            output.add(count + 1);
                                            _collector.emit(fountainStream, input, output);
                                    } else {
                                            output.add(drop);
                                            _collector.emit(gullyStream, input, output);
                                    }
     
                            }
                            _collector.ack(input);
                    }
     
                    @Override
                    public void declareOutputFields(OutputFieldsDeclarer declarer) {
                            declarer.declareStream(fountainStream, new Fields("drop", "use"));
                            declarer.declareStream(gullyStream, new Fields("drop"));
                    }
     
     
            }
     
            private static class GullyBolt extends BaseRichBolt {
     
                    private static final long serialVersionUID = 2758474522361204980L;
                    private OutputCollector _collector;
     
                    private int count = 0;
                    private Logger log;
     
                    @SuppressWarnings("rawtypes")
                    @Override
                    public void prepare(Map stormConf, TopologyContext context,
                                    OutputCollector collector) {
                            this._collector = collector;
                            this.log = Logger.getLogger("Gully");
                    }
     
                    @Override
                    public void execute(Tuple input) {
                            if (count++ % 1000 == 0) log.info(input.getString(0));
                            _collector.ack(input);
                    }
     
                    @Override
                    public void declareOutputFields(OutputFieldsDeclarer declarer) {
                            // nothing to declare, sir!
                    }
     
            }
     
            public static void main(String[] args) throws Exception {
                    TopologyBuilder builder = new TopologyBuilder();
     
                    builder.setSpout("rain", new WaterSpout(), 1);
                    builder.setBolt("fountain", new FountainBolt(), 1)
                            .shuffleGrouping("rain")
                            .shuffleGrouping("fountain", fountainStream);
                    builder.setBolt("gully", new GullyBolt(), 1)
                            .shuffleGrouping("fountain", gullyStream);
     
                    StormTopology topology = builder.createTopology();
     
                    Config conf = new Config();
     
                    System.out.println("Using local cluster");
     
                    new LocalCluster().submitTopology("rainyday", conf, topology);
     
            }
    }

