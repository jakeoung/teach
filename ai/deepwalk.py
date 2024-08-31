import marimo

__generated_with = "0.7.9"
app = marimo.App(layout_file="layouts/deepwalk.slides.json")


@app.cell
def __(mo):
    mo.md(
        """

        Naive attempt to implement DeepWalk for an instructive purpose. This code is not efficient. DeepWalk is a method to learn node embeddings from a graph. The idea is to use Skipgram with negative sampling to learn embeddings of nodes in a graph.\n\n    Reference

        - https://arxiv.org/abs/1403.6652
        - https://colab.research.google.com/github/chaklam-silpasuwanchai/Python-fo-Natural-Language-Processing/blob/main/Code/01%20-%20Fundamental/02%20-%20Word2Ve%20%28Negative%20Sampling%29%20from%20Scratch.ipynb#scrollTo=P598vUcveI3Q\n\n\

        ## 1. Load graph (EDA)\n
        """
    )
    return


@app.cell
def __():
    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    import numpy as np
    import matplotlib.pyplot as plt
    from sklearn.manifold import TSNE
    import networkx as nx
    G = nx.krackhardt_kite_graph()
    num_nodes = len(G.nodes())
    nx.draw_networkx(G, with_labels=True)
    plt.show()
    A = nx.adjacency_matrix(G).todense()
    D = np.sum(A, axis=0)
    Dinv = np.diag(1.0 / D)
    R = Dinv.dot(A)
    print(R)
    plt.imshow(R)
    plt.colorbar()
    return A, D, Dinv, F, G, R, TSNE, nn, np, num_nodes, nx, plt, torch


@app.cell
def __(R, np):
    ## 2. Random walk from a graph G
    # It corresponds to sampling a sequence of words in word2vec

    def random_walk(R, walk_length=3):
        """
        Generate a random walk by R.

        Args:
            R: Transition matrix.
            walk_length: Length of the random walk.

        Returns:
            A list of nodes in the random walk.
        """
        current_node = np.random.choice(range(len(R)))
        walk = [current_node]
        for _ in range(walk_length - 1):
            next_node = np.random.choice(range(len(R)), p=R[current_node])
            walk.append(next_node)
            current_node = next_node
        return walk
    walk = random_walk(R)
    walk
    return random_walk, walk


@app.cell
def __(mo):
    mo.md("\n    ## 3. Prepare train data\n")
    return


@app.cell
def __(R, np, num_nodes, random_walk):
    def random_batch(batch_size, walk_length, num_neg_samples=3):
        inputs = np.zeros((batch_size, 1), dtype=np.int32)
        labels = np.zeros((batch_size, 1), dtype=np.int32)
        neg_samples = np.zeros((batch_size, num_neg_samples), dtype=np.int32)
        for i in range(batch_size):
            walk = random_walk(R, walk_length)
            inputs[i, :] = walk[0]
            idx_rand = np.random.randint(walk_length - 1) + 1
            labels[i, :] = walk[idx_rand]
            idx_not_used = np.where(~np.isin(range(num_nodes), walk))[0]
            neg_samples[i, :] = np.random.choice(idx_not_used, num_neg_samples, replace=False)
        return (inputs, labels, neg_samples)

    batch_size = 2
    (inputs, labels, neg_samples) = random_batch(batch_size, 3)
    print('inputs:', inputs)
    print('labels:', labels)
    print('neg_samples:', neg_samples)
    return batch_size, inputs, labels, neg_samples, random_batch


@app.cell
def __(mo):
    mo.md("\n    ## 4. Model\n")
    return


@app.cell
def __(nn, torch):
    class DeepWalk(nn.Module):

        def __init__(self, num_nodes, embedding_dim):
            super(DeepWalk, self).__init__()
            self.num_nodes = num_nodes
            self.embedding_dim = embedding_dim
            self.embedding = nn.Embedding(num_nodes, embedding_dim)
            self.logsigmoid = nn.LogSigmoid()

        def forward(self, inp, target, neg_samples):
            start_emb = self.embedding(inp)
            target_emb = self.embedding(target)
            neg_embed = -self.embedding(neg_samples)
            pos_score = target_emb.bmm(start_emb.transpose(1, 2)).squeeze(2)
            neg_score = neg_embed.bmm(start_emb.transpose(1, 2))
            loss = self.logsigmoid(pos_score) + torch.sum(self.logsigmoid(neg_score), 1)
            return -torch.mean(loss)
    return DeepWalk,


@app.cell
def __(mo):
    mo.md("\n    ## 5. Train\n")
    return


@app.cell
def __(DeepWalk, num_nodes, plt, random_batch, torch):
    _batch_size = 10
    embedding_size = 2
    num_neg_samples = 3
    walk_length = 2
    model = DeepWalk(num_nodes, embedding_dim=embedding_size)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.002)
    epochs = 5000
    loss_save = []
    for epoch in range(epochs):
        (inp_batch, target_batch, neg_samples_batch) = random_batch(_batch_size, walk_length, num_neg_samples)
        inp_batch = torch.LongTensor(inp_batch)
        target_batch = torch.LongTensor(target_batch)
        neg_samples_batch = torch.LongTensor(neg_samples_batch)
        optimizer.zero_grad()
        loss = model(inp_batch, target_batch, neg_samples_batch)
        loss.backward()
        optimizer.step()
        if epoch % 10 == 0:
            loss_save.append(loss.item())
        if epoch % 100 == 0:
            print(f'Epoch {epoch + 1}, Loss: {loss.item()}')
    plt.plot(loss_save)
    return (
        embedding_size,
        epoch,
        epochs,
        inp_batch,
        loss,
        loss_save,
        model,
        neg_samples_batch,
        num_neg_samples,
        optimizer,
        target_batch,
        walk_length,
    )


@app.cell
def __(mo):
    mo.md("\n    # 6. Visualization\n")
    return


@app.cell
def __(G, TSNE, embedding_size, model, num_nodes, nx, plt, torch):
    nx.draw_networkx(G, with_labels=True)
    plt.title('original graph')
    plt.show()
    vecs = model.embedding(torch.LongTensor(range(num_nodes)))
    vecs_np = vecs.detach().numpy()
    if embedding_size > 2:
        tsne = TSNE(n_components=2)
        vecs_embedded = tsne.fit_transform(vecs_np)
        plt.figure(figsize=(6, 6))
        plt.scatter(vecs_embedded[:, 0], vecs_embedded[:, 1])
        for (i, (x, y)) in enumerate(vecs_embedded):
            plt.text(x, y, str(i), fontsize=8)
    else:
        plt.scatter(vecs_np[:, 0], vecs_np[:, 1])
        for (i, (x, y)) in enumerate(vecs_np):
            plt.text(x, y, str(i), fontsize=8)
    plt.title('embedding vectors')
    plt.show()
    return i, tsne, vecs, vecs_embedded, vecs_np, x, y


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()
