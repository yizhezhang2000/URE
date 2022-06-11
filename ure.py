def URE(scores,conf, requirement=0.9):
    index = np.argsort(-conf); tau_s=1.0; p_s=0
    for id in range(len(index)):
        pool=scores[index[:id+1]]; statistics=[];
        for b in range(1,100): # Bootstrapping for CI
            poolB=np.random.choice(pool, len(pool));
            stat=np.mean(poolB); # can be of other statistics
            statistics.append(stat);
        ordered = np.sort(statistics)
        lower = np.percentile(ordered, 2.5)
        if lower>=requirement:
            tau_s=conf[index[id]];p_s=len(pool)/len(scores);
    return tau_s, p_s
