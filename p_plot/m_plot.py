import matplotlib.pyplot as plt

def ploti(similar_song, column):
    plt.style.use('Solarize_Light2')
    boxprops = dict(linewidth=3, color='darkgoldenrod')
    fig, ax1 = plt.subplots(nrows=1, figsize=(7,4),dpi=75)
    ax1.boxplot(similar_song.head(50)[column],
        zorder=2,notch=True, patch_artist=True,
            boxprops=dict(linestyle='--', linewidth=3,facecolor='lightseagreen', color='darkgoldenrod'),
            capprops=dict(color='darkgoldenrod',linewidth=3),
            whiskerprops=dict(color='darkgoldenrod',linewidth=3),
            flierprops=dict(marker='o',color='black', markerfacecolor='lightseagreen',markeredgecolor='darkgoldenrod'),
            medianprops=dict(color='darkorange',linewidth=3),
            )
    ax1.boxplot(similar_song.head(1)[column],zorder=2,medianprops=dict(color='lightcoral',linewidth=3))
    ax1.set_ylim([similar_song.head(50)[column].min(), similar_song.head(50)[column].max()]) 
    plt.title(column, 
        fontdict={'family': 'Gotham', 
                    'color' : 'dimgrey',
                    'size': 18})
    plt.show()
    return plt.savefig(f"./Images/image/{column}.png")
