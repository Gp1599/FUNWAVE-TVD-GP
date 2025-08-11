import numpy as np
import matplotlib.pyplot as plt

def execute(Nh, Nw, gap, marg_h, marg_w):
    #% tight_subplot creates "subplot" axes with adjustable gaps and margins
    #%
    #% [ha, pos] = tight_subplot(Nh, Nw, gap, marg_h, marg_w)
    #%
    #%   in:  Nh      number of axes in hight (vertical direction)
    #%        Nw      number of axes in width (horizontaldirection)
    #%        gap     gaps between the axes in normalized units (0...1)
    #%                   or [gap_h gap_w] for different gaps in height and width 
    #%        marg_h  margins in height in normalized units (0...1)
    #%                   or [lower upper] for different lower and upper margins 
    #%        marg_w  margins in width in normalized units (0...1)
    #%                   or [left right] for different left and right margins 
    #%
    #%  out:  ha     array of handles of the axes objects
    #%                   starting from upper left corner, going row-wise as in
    #%                   subplot
    #%        pos    positions of the axes objects
    #%
    #%  Example: ha = tight_subplot(3,2,[.01 .03],[.1 .01],[.01 .01])
    #%           for ii = 1:6; axes(ha(ii)); plot(randn(10,ii)); end
    #%           set(ha(1:4),'XTickLabel',''); set(ha,'YTickLabel','')

    #% Pekka Kumpulainen 21.5.2012   @tut.fi
    #% Tampere University of Technology / Automation Science and Engineering
    ha = None
    pos = None
    #if nargin < 3: 
    #    gap = .02
    #if nargin < 4 or np.isempty(marg_h): 
    #    marg_h = .05
    #if nargin < 5: 
    #    marg_w = .05

    def numel(array):
        count = 0
        for i in array:
            if i is np.ndarray:
                for j in i:
                    count += 1
            else:
                count += 1
        return count
    
    if numel(gap) == 1: 
        gap = np.concatenate(arrays = [gap, gap])
    if numel(marg_w) == 1:
        marg_w = np.concatenate(arrays = [marg_w, marg_w])
    if numel(marg_h) == 1:
        marg_h = np.concatenate(arrays = [marg_h, marg_h])

    axh = (1 - sum(marg_h) - (Nh - 1) * gap[0]) / Nh 
    axw = (1 - sum(marg_w) - (Nw - 1) * gap[1]) / Nw

    py = 1 - marg_h[1] - axh

    ha = np.zeros(Nh * Nw)
    ii = 0
    for ih in range(0, Nh):
        px = marg_w[0]
        
        for ix in range(0, Nw):
            #ha(ii) = axes('Units','normalized', ...
            #    'Position',[px py axw axh], ...
            #    'XTickLabel','', ...
            #    'YTickLabel','');
            ha[ii] = np.array([px, py, axw, axh]) #plt.axes([px, py, axw, axh])
            px = px + axw + gap[1]
            ii = ii + 1
        py = py - axh - gap[0]
    
    #if nargout > 1:
    #    pos = plt.get(ha, 'Position')
    ha = ha[:]
    return ha, pos